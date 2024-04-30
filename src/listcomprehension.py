squarelist=[ value ** 2  for value in range(1,11)]

print(squarelist)


'''work with part of a list'''

print(squarelist[:4])


print(squarelist[0::2])

'''create  a players  list  , print them using for .. in loop  , their name in title case'''

my_fav_foods = ['pizza','falafel','carrot cake']
'''here i am retrieveing the complete list ignoring to give first and last index'''
friends_fav_foods=my_fav_foods[:]

print(my_fav_foods)

print(friends_fav_foods)

my_fav_foods.append('ice cream')

friends_fav_foods.append('tacos')

print(my_fav_foods)

print(friends_fav_foods)


'''best friend list of fav foods is exactly same as mine'''

bestie_fav_foods =  my_fav_foods

my_fav_foods.append('falooda')

print(bestie_fav_foods)



