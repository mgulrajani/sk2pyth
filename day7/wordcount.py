from pathlib import Path

def count_words(path):
    '''count number of workds in  a file'''

    try:
        contents  = path.read_text()
    except FileNotFoundError as f:
        print(f"Sorry {path} does not exist")
    else:
        words = contents.split()
        num_words =len(words)
        print(f"The file {path} has {num_words} words")


  