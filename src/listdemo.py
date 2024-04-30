bicycles = ['trek','cannondale','redline','specialized']

print(bicycles[-1].title())

print(bicycles[-2].title())


message = f"My first bicycle was a {bicycles[0].title()}."

print(message)


motorcycles = ['honda','yamaha','suzuki']

print(motorcycles)

motorcycles[0]='ducati'

print(motorcycles)

motorcycles.append('honda')
print(motorcycles)


fav_foods =[1,2]

fav_foods.append('apple')

fav_foods.insert(0,'mango')

del fav_foods[0]

print(fav_foods)
fav_foods.insert(0,'mango')

print(fav_foods)

popped_fruit =  fav_foods.pop()

print(popped_fruit)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(f"\n A {too_expensive.title()} is too expensive right now to be in the list")

#permanent sorting ,changes the list order permanently in the alphabetical order
motorcycles.sort()

print(motorcycles)

motorcycles.sort(reverse=True)

print(motorcycles)

numlist = [45,67,2,4,6,1,100,100]

numlist.sort()

print(numlist)


#sorted() method is for temporary sorting

cars = ['bmw' , 'audi' ,'toyota','subaru']

print(cars[-1])

cars2=[]

for car in cars:
    print(car)

#for item in list/set/collection
    

print(sorted(cars,reverse=True))

print(cars)

length = len(cars)

magicians = ['tom','jerry','pluto']


'''
for ( String magician : magicians ){

//logic
}


for item in list:
    line1
    line2
    line3

write the remaining code    
'''
for magician in magicians:
    print(f"{magician.title()} , that was a great trick!")
    
print(f"I cant wait to see your next trick!!")
