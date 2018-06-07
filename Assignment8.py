print("Question 1")
#Question 1
print("""TIME TUPLE
Many of Python's time functions handle time as a tuple of 9 numbers, as shown below -

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST""")
print("Question 2")
#Question 2
import time
t=time.gmtime()
print(t)
print(time.asctime(t))
print(time.ctime(3000))
print(time.ctime())
print("Question 3")
#Question 3
import datetime
from datetime import date
d=date.today()
print(d)
print("Month: ",d.month)
print("Question 4")
#Question 4
print("Day: ",d.day)
print("Question 5")
#Question 5
s=datetime.date(2021,6,16)
print(s)
print(s.day)
print("Question 6")
#Question 6
print("Local Time: ",time.localtime())
print("Question 7")
#Question 7
import math
num=int(input("Enter a number: "))
print("Factorial: ",math.factorial(num))
print("Question 8")
#Question 8
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("GCD: ",math.gcd(a,b))
print("Question 9")
#Question 9
import os
print(os.getcwd())
print(os.environ)