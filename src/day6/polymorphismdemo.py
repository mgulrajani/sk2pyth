'''
demo on subclassing dict 

'''

class NewDict(dict):
    def __setitem__(self, key, value) -> None:
        super().__setitem__(key,[value]*2)

    
    def __getitem__(self, key) :
        return super().__getitem__(key)
    
    

dictionary1 = NewDict(one=1)
dictionary1['two']=2
dictionary1['three']=3

print(dictionary1)
