from pathlib import Path
import json


numbers = [3,4,5,6,7]

path = Path('jsondata.txt')

content =  json.dumps(numbers)

path.write_text(content)

