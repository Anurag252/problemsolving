import os
import subprocess
from datetime import datetime
import re
import html

# Paths
REPO_DIR = '.'
TARGET_DIR = './chirpy'

# Language mapping
LANG_MAP = {
    ".py": "python",
    ".rs": "rust",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".js": "javascript",
    ".ts": "typescript",
    ".go": "go"
}

# Get last commit info
def get_commit_info(file_path):
    result = subprocess.run(
        ["git", "log", "--follow", file_path],
        cwd=REPO_DIR,
        capture_output=True,
        text=True
    )
    if result.stdout.strip():
        ln = result.stdout.strip().split("\n")
        commit_msg = ln[3:]
        commit_date_str = ln[2].replace("Date:").strip()
        commit_date = datetime.strptime(commit_date_str, "%a %b %d %H:%M:%S %Y %z")
        return commit_date, commit_msg
    return None, None

# Convert HTML to Markdown and ensure all links use https
def html_to_markdown(html_content):
    text = html_content
    text = re.sub(r'<(script|style).*?>.*?</\1>', '', text, flags=re.DOTALL).lstrip()
    text = re.sub(r'<h[1-6]>\s*(.*?)</h[1-6]>', r'## \1', text).lstrip()
    # Convert links to Markdown and force https
    def replace_link(m):
        url = m.group(1).replace("http://", "https://")
        label = m.group(2)
        return f"[{label}]({url})"
    text = re.sub(r'<a .*?href="(.*?)".*?>(.*?)</a>', replace_link, text)
    text = re.sub(r'<img .*?src=[\'"](.*?)[\'"].*?>', r'![image](\1)', text)
    text = re.sub(r'<(b|strong)>(.*?)</\1>', r'**\2**', text)
    text = re.sub(r'<(i|em)>(.*?)</\1>', r'*\2*', text)
    text = re.sub(r'<pre>(.*?)</pre>', lambda m: f'```\n{html.unescape(m.group(1))}\n```', text, flags=re.DOTALL)
    text = re.sub(r'<p.*?>', '\n\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return html.unescape(text.strip())

# Extract problem statement
def extract_problem_statement(solution_folder):
    readme_path = os.path.join(REPO_DIR, solution_folder, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        markdown_text = html_to_markdown(html_content)
        return markdown_text.lstrip()
    return "Problem statement not found."

# Ensure target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# Process all solution files
for root, _, files in os.walk(REPO_DIR):

    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in LANG_MAP:
            solution_file = os.path.join(root, file)
            lang_tag = LANG_MAP[ext]

            commit_date, commit_msg = get_commit_info(solution_file)
            if not commit_date:
                continue

            solution_folder = os.path.relpath(root, REPO_DIR)
            problem_statement = extract_problem_statement(solution_folder)

            # Frontmatter (metadata only)
            title = os.path.basename(root).replace("-", " ").title()
            tags = [lang_tag]
            frontmatter = f"""---
            title: "{title}"
            date: "{commit_date.isoformat()}"
            categories: ["leetcode"]
            tags: [{', '.join(tags)}]
            layout: post
---
            """

            # Read solution code
            with open(solution_file, "r", encoding="utf-8") as f:
                code_content = f.read()

            # Build Markdown content with {% raw %} around code
            md_content = f"""{frontmatter}
{problem_statement}

{{% raw %}}


```{lang_tag}


{code_content}


{{% endraw %}}
```
"""
                    # Save with date-prefixed filename
            date_prefix = commit_date.strftime("%Y-%m-%d")
            safe_title = title.replace(' ', '-')
            target_file_name = f"{date_prefix}-{safe_title}.md"
            target_file_path = os.path.join(TARGET_DIR, target_file_name)
            with open(target_file_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"Saved: {target_file_name}")
