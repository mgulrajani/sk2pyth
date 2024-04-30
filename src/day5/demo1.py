'''A class to represent a Book'''
class Author:
    '''modeling an Author'''

    def __init__(self,id=None,name=None,email=None,mobileNumber=None) -> None:
        self.id = id
        self.name= name
        self.email = email
        self.mobileNumber = mobileNumber


    def getDetails(self):
        details = f"{self.name} {self.email} {self.mobileNumber}"
        return details
    
 
    

'''Book (composition) has a author of Author type , Book has id of String type , title of String type, dop of String type'''      
class Book:
    '''modeling a Book'''

    def __init__(self,id,title,author,dop) -> None:
        self.id = id
        self.title = title
        self.dop = dop
        self.author =Author(author.id,author.name,author.email,author.mobileNumber)

    
    def get_details(self):
        pass

    def update_dop(self,dop):
        self.dop=dop

    def __str__(self) -> str:
        details = f"{self.title} {self.author.name} {self.author.email} {self.dop}"
        return details
    

'''DigitalBook is a Book
or is "DigitalBook has  a Book" correct ?'''

class DigitalBook(Book):
    '''Modeling aspect of a Book ,specific to DigitalBook'''

    def __init__(self, id, title, author, dop,filesize) -> None:
        super().__init__(id, title, author, dop)
        self.filesize=filesize

    def get_details(self):
       pass
    #overriding parent class update_dop 
    def update_dop(self,dop):
        super().update_dop(dop)
        print('updating dop')

    '''if we dont override __str__ , when we print the object  , we get mem location,we want a string of this object'''
    def __str__(self) -> str:
      details=f" {super().__str__()}  File Size in Kbs {str(self.filesize)}"
      return details
    
