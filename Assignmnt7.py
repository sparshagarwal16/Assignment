print("Question 1")
#Question 1
r=int(input("Enter raius of the circle: "))
def area(r):
    a=3.14*r*r
    return a
print("Area of the sphere is ",area(r)," square units")
print("Question 2")
#Question 2
def perfect(i):
    f=0
    for k in range(1,i):
        if(i%k==0):
            f=f+k
    if(f==i):
        print(i," is a perfect number ")
for j in range(1,1000):
    perfect(j)
print("Question 3")
#Question 3
def table(n,time=1):
    if time <= 12:
        print(n,"X", time,"=", n*time)
        table(n, time+1)
    else:
        return
table(12)
print("Question 4")
#Question 4
def power(a,b):
    if(b==0):
        return 1
    else:
        return a*power(a,b-1)
a=int(input("Enter the base number: "))
b=int(input("Enter the power: "))
print(power(a,b))
print("Question 5")
#Question 5
dict={}
def fact(num):
    if(num==1):
        return num
    else:
        return num*fact(num-1)
num=int(input("Enter a number: "))
dict[num]=f=fact(num)
print("Factorial")
print(dict)