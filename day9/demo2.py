import methods as m
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f'Starting task {id}')
    sleep(1)
    return f'Done with task {id}'



""" with ThreadPoolExecutor() as executor:
    f1 =executor.submit(task,1)
    f2 =executor.submit(task,2)
    f3 =executor.submit(task,3)
    print(f1.result())
    print(f2.result())
    print(f3.result())
    
 """

with ThreadPoolExecutor(max_workers=2) as service:
    list1 = [1,2,3,4]
    list2=[5,6,7,8]
    list3 = [9,10,11,12]

    results = service.map(m.calc_cube,[list1,list2,list3])
    for result in results:
        print(result)
