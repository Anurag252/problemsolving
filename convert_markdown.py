import os
import markdown2
import shutil

def convert_markdown_to_html(md_file):
    html_file = os.path.splitext(md_file)[0] + '.html'
    with open(md_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
        html_content = markdown2.markdown(markdown_content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_index(directory):
    index_file = os.path.join(directory, 'index.html')
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Index</title>\n</head>\n<body>\n')
        f.write(f'<h1>Index of {directory}</h1>\n<ul>\n')
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.html') and filename != 'index.html':
                f.write(f'<li><a href="{filename}">{filename}</a></li>\n')
        f.write('</ul>\n</body>\n</html>\n')

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                md_file = os.path.join(root, file)
                print( "converting file-", md_file)
                convert_markdown_to_html(md_file)

        for directory in dirs:
            directory_path = os.path.join(root, directory)
            generate_index(directory_path)

        for directory in dirs:
            try:
                new_directory_path = os.path.join(root, "dist")
                if not os.path.exists(new_directory_path):
                   os.makedirs(new_directory_path)
                old_directory_path = os.path.join(root ,directory)
                if os.path.isfile(f"{old_directory_path}/{directory}.html"):
                    shutil.move(f"{old_directory_path}/{directory}.html", f"{new_directory_path}/{directory}.html")
            except OSError as exc:
                pass
            

if __name__ == "__main__":
    main()
