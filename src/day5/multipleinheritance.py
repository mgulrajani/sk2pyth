class Animal:
    def get_details(self):
        print("Animal is abstract")


class Bird:
    def get_details2(self):
        print("Bird is also abstract")

class Mammal(Animal):
    def get_details3(self):
        print("Mammals have their own features")

class Bat(Mammal,Bird):
    def get_details(self):
        print(super().get_details3())
        print(super().get_details2())



    

class A:
    def m1(self):
        print("In Class A")


class B:
    def m1(self):
        print("In Class B")


class C(A):
    def m1(self):
        print("In Class C")


class D(B,C):
    pass
    """ def m1(self):
        print("In class D")
 """

obj =D()

obj.m1()

