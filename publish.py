import os
import frontmatter
from shutil import *
import os

if not os.path.exists('./_notes'):
    os.mkdir('./_notes')

original = "../zettelkasten/Spaces/Projects/Bible Study Kit/Scripture (BPT)/"
target = "./_notes/"
move(original, target)

for file in os.listdir("../zettelkasten/"):
    if file.endswith(".md"):
        with open(os.path.join("../zettelkasten/", file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys() and metadata['publish'] == True:
                print("Copy publish files from zettelkasten to _notes/")
                copy(os.path.join("../zettelkasten/", file), './_notes/')
            else:
                pass

for root, dirs, files in os.walk("../zettelkasten/Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys() and metadata['publish'] == True:
                    print("Copy publish files from zettelkasten to _notes/")
                    print(os.path.join(root, file))
                    copy(os.path.join(root, file), './_notes/')
                else:
                    pass
