import os
import json
import tempfile
import subprocess


with open("filenames.json") as jf:
    filenames = json.load(jf)

with open("extensions.json") as jf:
    extensions = json.load(jf)

with open("formats.json") as jf:
    formats = json.load(jf)


def clone_and_list_files(repo_url):
    def get_format(file):
        filename_data = filenames.get(file)
        if filename_data:
            return filename_data
    
        extension = os.path.splitext(file)[1]
        extension_data = extensions.get(extension)
        if extension_data:
            return extension_data
        
        return {}

    with tempfile.TemporaryDirectory() as tmpdirname:
        subprocess.run(['git', 'clone', '--depth', '1', repo_url, tmpdirname], check=True)

        file_list = []

        for root, dirs, files in os.walk(tmpdirname):
            if '.git' in dirs:
                dirs.remove('.git')
            for file in files:
                file_list.append({
                    "name": file,
                    "size": os.path.getsize(os.path.join(root, file)),
                    "format": get_format(file)
                })

    return file_list

                

# Example usage:
result = clone_and_list_files("https://github.com/gijs6/havas.git")

print(json.dumps(result, indent=4))
