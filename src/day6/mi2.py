from multipleinheritancedemo2 import A

class C():
    def ping(self):
        print(f'{self}.ping() in C')
        super().ping()

class Leaf(A,C):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()

    

leaf = Leaf()
leaf.ping()
