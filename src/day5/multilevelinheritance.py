from math import pi

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b) -> None:
        super().__init__()
        self.length = l
        self.breadth = b

    def calculate_area(self):
        return self.length * self.breadth
    


class Square(Rectangle):
    def __init__(self, l) -> None:
        super().__init__(l, l)

    def calculate_area(self):
        return self.length ** 2
    

class Circle(Shape):
    def __init__(self,r) -> None:
        super().__init__()
        self.radius = r

    def calculate_area(self):
        return pi*self.radius**2
    
    

