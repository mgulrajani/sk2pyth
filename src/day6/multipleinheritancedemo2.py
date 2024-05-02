class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    
    def pong(self):
         print(f'{self}.pong() in Root')

    def __repr__(self) -> str:
        cls_name=type(self).__name__
        return f'<instance of {cls_name}'
    

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()


    
    def pong(self):
         print(f'{self}.pong() in A')
         super().pong()
    

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()


    
    def pong(self):
         print(f'{self}.pong() in B')
         super().pong()
    


class Branch(B,A):
    def ping(self):
        print(f'{self}.ping() in Branch')

'''  


branch = Branch()

branch.ping()
branch.pong()
print(Branch.__mro__)

'''
'''
special functions

__init__()  constructor , it initializes attributes of the object

__str__()   string representation of the object

__len__() 

__add__()



'''