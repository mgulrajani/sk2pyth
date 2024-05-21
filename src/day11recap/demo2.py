import demo3 as d

num=[4,5,6,7,20,4.5,True ,"hetal",[2,3,4,5,"data"]]
print(num[8][0])

num[5]=100

print(num)

print(id(num))


a=[4,5,6]
print(len(a))
a.append(9)
a.insert(2,10)
print(f"before pop {a}")

try:

    a.remove(20)
except:
    print("item does not exist in the list")
print(f"max of the list {max(a)}")

a.sort()
print(f"original a {a}")
temp_a =sorted(a)
print(f"sorted list {temp_a}")

b=a[:]
print(b)
b[0]=100
print(a)
print(b)

for num in a:
    print(num)



for a  in range(1,100,10):
    print(a)


for num in range(5):
   #TODO : add code to print numbers

   pass


health =10

while health > 0:
    print(health)
    health-=1



for i in range(3):
    for j in range(4):
        print(i,j)


nums = []

if not nums:
    print("empty")


d.printInfo("kajal",20)
d.printInfo("ajay",12)
d.printInfo(age=34,name="kailash")

list=[1,2,3,4]

d.squares(list)


d.calcArea(2)
d.calcArea(3)

d.calcArea(4)


d.printName("john","smith")
d.printName("john","smith","paul")

d.printData("Alex John",4,5,True,"Jess")


d.printOutputData(name="Alex Jess",age=22)
d.printOutputData(name="Mihika  ",age=12,grade=3)
d.printOutputData(name="Meetali  ",age=12,school="Podar International")

