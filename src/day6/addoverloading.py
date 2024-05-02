class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def __str__(self):
        return '({0} {1})'.format(self.x,self.y)
    
    def __add__(self,otherPoint):
        x= self.x+otherPoint.x
        y=self.y+otherPoint.y
        return Point(x,y)
    

    def __gt__(self,otherPoint):
        return self.x > otherPoint.x and self.y > otherPoint.y
    
    



