from collections  import Counter,OrderedDict,UserString


c = Counter(['B','A','a',"b",'B','B','A','A'])


'''ordereddict  -- it remembers the insertion order  , means the order 
in which elements were inserted
'''

d=OrderedDict()

d['one']=1
d['three']=3
d['five']=5
d['two']  =2
d['six']=6
d['four']=4

d.pop('two')

for k,v in d.items():
    print(k,v)






