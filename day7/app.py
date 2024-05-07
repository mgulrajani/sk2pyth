from wordcount import count_words
from pathlib import Path


filenames = ['data.txt','day7/demo2.py' ,'day7/filelist.py']

for fn  in filenames:
    path = Path(fn)
    count_words(path)

