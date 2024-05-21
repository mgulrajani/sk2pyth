'''functions are defined in this module and will be called in other modules
'''
def printInfo(name,age):
    print(f"Hello {name} {age}")


def squares(numlist):
    for num in numlist:
        print(num**2)



def calcArea(r,pi=3.14):
    area = pi*(r**2)
    print(f"Area is {area}")



def printName(first,last,middle=""):
    if middle:
        print(f"{first} {middle} {last}")
    else:
        print(f"{first}  {last}")


def printData(name,*args):
    print(type(args))
    for arg in args:
        print(arg)



def printOutputData(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs)
