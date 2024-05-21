import logging
import time
from concurrent.futures import ThreadPoolExecutor
import threading

logger = logging.getLogger(__name__)
class Data:
    def __init__(self,value) -> None:
        self.value = value
        self._lock=threading.Lock()


    def update(self,name):
        #logger.info('Thread %s: starting update' ,name)
        print(f"Thread {name} starting update")
        print(f"Thread going to acquire lock {name}")
        with self._lock:
            local_copy =  self.value
            local_copy += 1
            time.sleep(0.3)
            self.value = local_copy
             #logger.info("Thread %s :finishing update", name)
            print(f"Thread {name} ending update {self.value}")

if __name__== '__main__':
    print('in main function')

    data = Data(5)
   # logger.info("Testing the value %d" ,data.value)
    print(f"testing the value {data.value}")

    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(1,10):
            executor.submit(data.update,i)
       # logger.info("Testing update .Ending value %d",data.value)
        print(f"Testing ending value after update {data.value}")


