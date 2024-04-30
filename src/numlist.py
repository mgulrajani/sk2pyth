for value in range(11):
    print(value)

'''
this will call the list c
'''
#numlist is the list with series of numbers from 1 to 10 
numlist =  list(range(1,11))

#here we are creating an empty list named squarelist
squarelist =[]

#using for in loop , individual element name is num and list name numlist
'''in the logic of for .. in loop we are squaring the number and appending it to the squarelist'''
for num in numlist:
    square  =num **2
    squarelist.append(square)


print(squarelist)    

print(max(squarelist))
print(min(squarelist))
print(sum(squarelist))


