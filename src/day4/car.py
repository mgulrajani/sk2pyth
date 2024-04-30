class Car:
    '''Attempting to model a Car'''

    def __init__(self,make,model,year) -> None:
        '''Initiaze attributes to describe a car'''
        self.make = make
        self.model=model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        details =  f"{self.year} {self.make} {self.model}"
        return details
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer_reading(self,mileage):
        self.odometer_reading=mileage



my_car =  Car('audi','a4',2024)

#my_car.odometer_reading  = 23
my_car.update_odometer_reading(23)
print(my_car.get_details())
my_car.read_odometer()




        