 describe_pet(pet_name,animal_type='dog',color=''):
    '''Displaying info about a pet'''
    #print(f"I have a {animal_type}")
    pet={'type':animal_type,'name':pet_name}
    if color:
         pet['color']= color
    
    return pet