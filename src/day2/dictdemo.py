'''
real world object -- key value pair 
key -- value attached which gives me more info about the key 

amazon
list of products 
click on one of the product link  , it fetches the details of that product

for eg : you are working on creating a game where you have set of aliens or set of players 


color and points 
green 5
red 15 

'''


alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
'''what is the value of color of alien_0'''
print(alien_0['color'])

'''what is the value of points of alien_0'''
indi_points =  alien_0['points']

print(indi_points)
'''here are using the syntax to add new key-value pairs to the alien_0 dictionary'''
alien_0['x-pos']=10
alien_0['y-pos']=100

print(alien_0)

alien_0['speed'] = 'medium'

print(f"Original position {alien_0['x-pos']}")

if alien_0['speed'] =='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3


alien_0['x-pos'] = alien_0['x-pos']+x_increment

print(f"New position of alien is {alien_0['x-pos']}")


#print(alien_0['point'])


pointval =  alien_0.get('point','No such key')

print(pointval)



for k,v in alien_0.items():
    print(f"Key is {k}")
    print(f"Value is {v}")


for k in alien_0.keys():
    print(f"Key is {k}")
    
for v in alien_0.values():
    print(f"Values are {v}")
    


fav_languages ={

  'john':'c',
  'smriti':'java',
  'megha':'c',
  'lakshmi':'js',
  'mitali':'python',
  'harsh':'python',
  'sameer':'java'


}

for lang in set(fav_languages.values()):
    print(lang)

aliens = []


for alien_num in range(10):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    print(alien)
    print('...')


print(f"Total number of aliens {len(aliens)}")


