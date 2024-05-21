import time
def calc_square(numlist):
    for i in numlist:
        print(f'\n{i} ^ 2 ={i*i}')
        time.sleep(0.3)
    return i*i


def calc_cube(numlist):
    for i in numlist:
        print(f'\n{i} ^ 3 ={i*i*i}')
        time.sleep(0.3)
    return i*i*i

