'''we are going to write a program to read from  a file for which we
are specifying a Path , if the file does not exist ,right now just
print a message that file does not exist  , later you can take care
of exception handling 
read the file - -  input 
write to the file  --output
'''
''' / linux 
\\  in the windows path

'''
from pathlib import Path
import os
path = Path('src/greetings.txt')

doesExist=path.exists()

if doesExist:
    content =  path.read_text()
  
lines =content.splitlines()

for line in lines:
    print(line)


data3 = 'learning to write to files in Python'
data3 += '\nloving to work with files at os level with pathlib Path'
data3 += '\n its so much easier than os level module'

p1 =Path('data2.txt')

p1.write_text(data3)

