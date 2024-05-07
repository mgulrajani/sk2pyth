import os

entries = os.listdir('src/')

for entry in entries:
    print(entry)
    

with open('data.txt','w') as f:
    data = 'python is great to work with files'
    f.write(data)


print('data written on to the file newly created ')    