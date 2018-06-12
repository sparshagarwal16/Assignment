#Question 1
print("Question 1")
import math
import time
import threading
from threading import Thread
def sleepme():
    print("Thread is sleeping", threading.currentThread().getName())
    time.sleep(5)
    print("Thread is awake",threading.currentThread().getName())
t=Thread(target=sleepme,args=())
t.start()
#Question 2
print("Question 2")
for i in range(1,11):
    print(i)
    time.sleep(1)
#Question 3
print("Question 3")
l=["Apple","Mango","Orange","Cranberry","Plum"]
s=2
for i in l:
    time.sleep(s)
    s=s+2
    print(i)
#Question 4
print("Question 4")
class factotial(threading.Thread):
    def __init__(self,number):
        threading.Thread.__init__(self)
        self.num=number
    def run(self):
        print(math.factorial(self.num),"\n")
threads=[]
while True:
    var=int(input("Enter a number: "))
    if(var<1):
     break
    thread=factotial(var)
    threads+=[thread]
    print(threads)
    thread.start()
for x in threads:
    x.join()

