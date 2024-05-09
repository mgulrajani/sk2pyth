import re

'''to create  a Pattern we have to compile it 
re is separate programming language which is embedded in python'''

'''to create a regular expression Pattern , we are using compile of re module , to that compile
method we are providing our regular expression 
i want to search only digits in a given str
\d  -digit class in re means digits  0-9 
\s  spaces
\w words

{ m,n}  min and n means max {2,5}'''

'''looking for digits 2 digit till max of 5 digits'''

digit_pattern = re.compile('\d{3,6}')

str2 ="good morning"

str = 'Welcome to Python 311 which has great support for oops ,released in 2022 455555 99999999 8989898 888888'

result = digit_pattern.findall(str)

print(result)

username = 'admin33344'

print(re.search('[0-9]*[^a-z]',username))


text = '23rea**aa]ba7667676767babding redabababg reaaddng reaad1ng read3ng aand playing chess and reaading ababababab    abababab  ababab'

pattern = r"[\]]"

print(re.search(pattern,text))

result = re.findall(pattern,text)
print(result)


s='this is BPython 4000 regular 6000 expression ,9000 re module of Python '

matches = re.finditer('\d{4}',s)

for match in matches:
    print(match)



phonenumber = '(+91)9988877766'

matches = re.finditer('\D',phonenumber)

for match in matches:
    print(match)

plainphonenumber =  re.sub('\D','',phonenumber)

print(plainphonenumber)


matches = re.finditer(r'\bPython\b',s)

for m in matches:
    print(m.group())

'''searching for text which is inside the  " " double quotes like in the below str text and username'''
htmlcode='<input type="text" name="username"/>'

pattern = '".+?"'

matches = re.finditer(pattern,htmlcode)

for m in matches:
    print(m.group())


password = 'apple999abc'

print(re.search('(apple)(\d{3})',password))

mgroups =re.search('(apple)(\d{3})(abc)',password)

'''whole group'''
print(mgroups[0])

'''first group'''
print(mgroups[1])

'''second group'''
print(mgroups[2])

print(mgroups[3])


list =  ["java",".net","oracle","js"]

for e in list:
    match = re.match("(\w+)",e)

    if (match):
        print(match.groups())


string_to_be_searched  = "Javascript is ES2016 standards implementation and it supports async programming "


pattern =  "(\w{10}).+(\d{4})"

result = re.match(pattern,string_to_be_searched,re.IGNORECASE)

print(result.groups())
