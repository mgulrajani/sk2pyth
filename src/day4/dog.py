class Dog:
    '''A simple attempt to model a Dog'''

    '''constructor takes , self (pointing to itself same object, this in Java) name and age'''
    def __init__(self,n,a) -> None:
        self.name=n
        self.age=a

    def sit(self):
        '''Simulating a dog sitting in response to a command'''
        print(f"{self.name} is now sitting")

    def roll_over(self):
        '''Simulating roll over in respones to a command'''
        print(f"{self.name} rolled over!")


my_dog= Dog('Willie',3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

my_dog= Dog('Snowy',2)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()



'''Make a class Restaurant . The __init__ method for Restaurant should store
two attributes restaurant_name and cuisine_type . Make a method called describe_restaurant()
that prints these two pieces of information and a method called open_restaurant() that
prints a message indicating that the restaurant is open

Make an instance called restaurant . print its 2 attributes and call 2 methods

'''



    