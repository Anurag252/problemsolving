from operator import __mod__
import os
import re
import markdown2
import textile
import shutil

class MarkdownToHTML:
        
    def list_all_files(self) -> list[str]:
        result = []
        input_ext = str(os.environ.get("input_ext", ".*"))
        for root, subdirs, files in os.walk(os.curdir):
            for name in files:
                for file_ext in input_ext.split(","):
                    if re.search(file_ext.strip(), name) != None:
                        list_file_path = os.path.join(root, name)
                        result.append(list_file_path)
        return result


    def convert_to_HTML(self, list_of_files: list[str]):
        for file in list_of_files:
            if file.endswith(".md") and not file.endswith(".html"):
                html_text = ""
                with open(file, 'r') as content_file:
                    content = content_file.read()
                    html_text= markdown2.markdown(content)
                
                root,ext = os.path.splitext(file)

                with open(root + ".html", 'w') as html_file:
                    html_file.write(html_text)
                self.copy_to_dist(root + ".html")
            
            elif file.endswith(".py") or file.endswith(".c") or file.endswith(".cs") and not file.endswith(".html"): # treat as text file
                html_text = ""
                with open(file, 'r', encoding='latin-1') as content_file:
                    content = content_file.read()
                    html_text= textile.textile(content)
                
                root,ext = os.path.splitext(file)
                with open(root + ".html", 'x') as html_file:
                    html_file.write(html_text)
                self.copy_to_dist(root + ".html")
                


    def copy_to_dist(self, file : str):
        print(file)
        _,file_in_dest = os.path.split(file)
        dest_path = "./dist/" + file_in_dest
        shutil.move(file, dest_path)


mktohtml = MarkdownToHTML()
list_of_files = mktohtml.list_all_files()
mktohtml.convert_to_HTML(list_of_files)