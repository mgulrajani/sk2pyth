cars = ['audi' , 'bmw' ,'subaru','toyota']

prefered_car = 'lamborgini'


for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())


if prefered_car  in cars:
    print(f"{prefered_car.title()} ,  in available car list")
else:
     print(f"{prefered_car.title()} ,  not in available car list")    


available_toppings = ['mushrooms' ,'extra cheese','pepperoni','pineapple','green peppers']
requested_toppings = ['mushrooms' ,'extra cheese','olives']

if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')




for request_topping in requested_toppings:
    print(f"Adding {request_topping}")


print("\n Finished making your pizza")




for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f" Sorry ,we dont have {requested_topping}")


print("\n Finished making your pizza")

'''assignment

make a list of five users -current_users (a b c d e)

make another list new_users(a b f g h)

if username exists print the message that that username is taken 
else print a  message username available

'''


