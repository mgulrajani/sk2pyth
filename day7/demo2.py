from pathlib import Path
import os

'''print all txt files '''

files = Path('src/')

for entry in files.iterdir():
    if entry.name.endswith('.txt'):
        print(entry.name)


dir1='src/'
with os.scandir(dir1) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.path)

            