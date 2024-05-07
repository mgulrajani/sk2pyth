from pathlib import Path
import json




path = Path('jsondata.txt')

contents= path.read_text()

nums =  json.loads(contents)

print(nums)





