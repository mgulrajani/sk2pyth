import math
def add(num1,num2):
    return num1+num2;


def divide(num1,num2):
    return num1/num2;


def sum(list):
    total = 0
    for val in list:
        total += val
    return total


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,radius) -> None:
        super().__init__() 
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius ** 2

    def perimeter(self):
        return 2*math.pi*self.radius
    


class Rectangle(Shape):
    def __init__(self,l,b) -> None:
        super().__init__() 
        self.l = l
        self.b=b
    
    def area(self):
        return self.l * self.b

    def perimeter(self):
        return (2*self.l)+(2*self.b)
    

class Square(Rectangle):

    def __init__(self,l) -> None:
        super().__init__(l,l) 
        self.l = l
        
       
    
    def area(self):
        return self.l * self.l


class Survey:
    """Model a Survey -- answers to questions"""

    def __init__(self,question) -> None:
        self.question = question
        self.responses = []

    
    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    
    def show_results(self):
        print("Survey results")
        for response in self.responses:
            print(f" -- {response}")

