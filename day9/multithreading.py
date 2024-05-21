import threading
import methods as m
import time


nums=[2,3,4,5,6,7]
start_time = time.time()
m.calc_square(nums)
m.calc_cube(nums)
end_time=time.time()

print("Execution time :{} ".format(end_time-start_time))
start_time=time.time()
t1=threading.Thread(target=m.calc_square,name="t1",args=(nums,))

t2=threading.Thread(target=m.calc_cube,name="t2",args=(nums,))

#thread should a life cycle of run , it will not immediately run

t1.start()

t2.start()


#t1 should run completely the run of callable target is calc_square
t1.join()  

t2.join()
endtime=time.time()

print("Execution time :{} ".format(end_time-start_time))



