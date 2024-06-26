import time
from threading import Thread

def nums(n):
    for x in range(1,11):
        time.sleep(1)
        print(x)

def chars():
    ch = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j']
    for x in ch:
        time.sleep(1)
        print(x)

thr_one = Thread(target=nums, args=(10, ))
thr_two = Thread(target=chars)

thr_one.start()
thr_two.start()

thr_one.join()
thr_two.join()
