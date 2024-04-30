
'''import the entire module  eg: import day4.pizza'''
'''from day4.pizza import makepizza'''
'''from day4.pizza import makepizza , f1'''
'''import day4.pizza as p'''
'''from day4.pizza import makepizza as mp'''

import src.day4.pizza as p
#definition of function
def greeting(username):
    '''Displaying a greeting to the user'''
    print(f"Hello!! {username.title()}")


#execute or call the function
    
greeting('jassi')


def describe_pet(pet_name,animal_type='dog',color=''):
    '''Displaying info about a pet'''
    #print(f"I have a {animal_type}")
    pet={'type':animal_type,'name':pet_name}
    if color:
         pet['color']= color
    
    return pet
while True:
    print("\n Please enter Pet details")
    print("\nPlease enter q to quit any time")

    type=input("Type")
    if type == 'q':
        break
    name=input("Name")
    color=input("Color")

 
    pet = describe_pet(animal_type=type,pet_name=name,color=color)
    print(pet)

""" 

val2 = describe_pet(pet_name='slowy',animal_type='turtle')
print(val2)

val2=describe_pet(pet_name='bolt',animal_type='dog',color='black')
print(val2)

val2=describe_pet('hunter',color='white')
print(val2)

val2 =describe_pet(pet_name='tiger',animal_type='tiger')
print(val2)
 """

#

def print_designs(unprinted_designs, completed_designs):
    '''it will 2 lists , one list which has uncompleted ,
    completed , pop from the first list and append in the second list
    '''
    while unprinted_designs:
        current_design =  unprinted_designs.pop()
        completed_designs.append(current_design)



def show_completed_designs(completed_designs):
    '''showing the completed designs'''
    for completed_design in completed_designs:
        print(completed_design)        


uncompleted_d = ['phone_case','robot pendant','unicorn']

compl=[]

print_designs(uncompleted_d[:],compl)

show_completed_designs(compl)
print('unmodified uncompleted d list')
print(uncompleted_d)



p.makepizza('12-inch','thin','cheese')

p.makepizza('16-inch','normal','mushrooms','olives','green peppers')


