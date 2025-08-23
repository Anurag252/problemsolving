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

def run_git(cmd, cwd=REPO_DIR):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)

# Get the FIRST commit (original) that added the file; return ISO author date + subject
def get_original_commit_info(file_path):
    # First (added) commit for this path, following renames, author date ISO, plus subject
    res = run_git(["git", "log", "--follow", "--diff-filter=A", "-1", "--format=%aI||%s", "--", file_path])
    out = res.stdout.strip()
    if out:
        date_iso, msg = out.split("||", 1)
        return date_iso, msg

    # Fallback: last commit that touched this path (if added-commit not found due to shallow history)
    res2 = run_git(["git", "log", "-1", "--format=%aI||%s", "--", file_path])
    out2 = res2.stdout.strip()
    if out2:
        date_iso, msg = out2.split("||", 1)
        return date_iso, msg

    return None, None

# Convert HTML-ish README to Markdown and ensure https links
def html_to_markdown(html_content):
    text = html_content

    # strip scripts/styles
    text = re.sub(r'<(script|style).*?>.*?</\1>', '', text, flags=re.DOTALL).lstrip()

    # normalize headings (avoid leading whitespace before ##)
    text = re.sub(r'<h[1-6]>\s*(.*?)\s*</h[1-6]>', r'## \1', text)

    # links -> markdown and force https
    def repl_link(m):
        url = m.group(1).replace("http://", "https://")
        label = m.group(2)
        return f"[{label}]({url})"
    text = re.sub(r'<a .*?href="(.*?)".*?>(.*?)</a>', repl_link, text)

    # images
    text = re.sub(r'<img .*?src=[\'"](.*?)[\'"].*?>', r'![image](\1)', text)

    # bold/italic
    text = re.sub(r'<(b|strong)>(.*?)</\1>', r'**\2**', text)
    text = re.sub(r'<(i|em)>(.*?)</\1>', r'*\2*', text)

    # preformatted blocks -> fenced
    text = re.sub(r'<pre>(.*?)</pre>', lambda m: f'```\n{html.unescape(m.group(1))}\n```', text, flags=re.DOTALL)

    # paragraphs and breaks
    text = re.sub(r'<p.*?>', '\n\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)

    # drop remaining tags
    text = re.sub(r'<.*?>', '', text)

    # collapse extra newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return html.unescape(text.strip())

def extract_problem_statement(solution_folder):
    readme_path = os.path.join(REPO_DIR, solution_folder, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return html_to_markdown(html_content).lstrip()
    return "Problem statement not found."

os.makedirs(TARGET_DIR, exist_ok=True)

generated = 0

for root, _, files in os.walk(REPO_DIR):
    # skip output folder and .git
    if os.path.relpath(root, REPO_DIR).startswith((".git", os.path.basename(TARGET_DIR))):
        continue

    for file in files:
        ext = os.path.splitext(file)[1]
        if ext not in LANG_MAP:
            continue

        solution_file = os.path.join(root, file)
        lang_tag = LANG_MAP[ext]

        # use original commit date (first time the file was added)
        commit_date_iso, commit_msg = get_original_commit_info(solution_file)
        if not commit_date_iso:
            # as a last resort, use filesystem mtime
            mtime = datetime.fromtimestamp(os.path.getmtime(solution_file)).astimezone()
            commit_date_iso = mtime.isoformat()

        solution_folder = os.path.relpath(root, REPO_DIR)
        problem_statement = extract_problem_statement(solution_folder)

        # Title from folder name
        title = os.path.basename(root).replace("-", " ").title()
        tags = [lang_tag]

        # Clean frontmatter (no indentation)
        frontmatter = (
            f"---\n"
            f"title: \"{title}\"\n"
            f"date: \"{commit_date_iso}\"\n"
            f"categories: [\"leetcode\"]\n"
            f"tags: [{', '.join(tags)}]\n"
            f"layout: post\n"
            f"---\n"
        )

        with open(solution_file, "r", encoding="utf-8") as f:
            code_content = f.read().rstrip()

        md_content = (
            f"{frontmatter}\n"
            f"{problem_statement}\n\n"
            f"{{% raw %}}\n"
            f"```{lang_tag}\n"
            f"{code_content}\n"
            f"```\n"
            f"{{% endraw %}}\n"
        )

        # Use original date for filename prefix
        try:
            dt = datetime.fromisoformat(commit_date_iso)
        except ValueError:
            # guard for any odd format; fallback to current
            dt = datetime.now().astimezone()
        date_prefix = dt.strftime("%Y-%m-%d")

        safe_title = title.replace(' ', '-')
        target_file_name = f"{date_prefix}-{safe_title}.md"
        target_file_path = os.path.join(TARGET_DIR, target_file_name)

        # Always write (so deleted files are re-generated)
        with open(target_file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        generated += 1
        print(f"Saved: {target_file_name}")

print(f"Done. Generated {generated} post(s).")
