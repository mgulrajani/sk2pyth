'''you want to accept arbitrary number of args ,but if you are not aware of the kind of information that will be passed to the function '''

'''in that case you can write functions which can accept as many key-value pairs ,calling statements'''


def build_profile(first,last,**user_info):
    '''Build a dictionary containing info about a user'''
    user_info['firstname']= first
    user_info['lastname']=last
    return user_info


""" user_profile =  build_profile('albert','einstein',location='princeton',field='physics',hobbies=['reading','skiing'])


print(user_profile)

 """

'''write a function that stores information about a car in a dictioary.
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments .
Call the function with required information and two other name-value pairs'''






