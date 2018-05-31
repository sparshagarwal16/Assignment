print ("Question 1")
#Question 1
l=[]
n=int(input("Enter number of values in the list "))
for i in range(n):
    val=input("Enter a value ")
    l.append(val)
print(l)
print ("Question 2")
#Question 2
s=["Google","Apple","Facebook","Tesla"]
l.extend(s)
print (l)
print ("Question 3")
#Question 3
w=["Orange","Apple","Banana","Apple"]
print(w.count("Apple"))
print("Question 4")
#Question 4
num=[3,4,56,34,97]
num.sort()
print(num)
print("Question 5")
#Question 5
a=[3,23,56,43,5]
b=[2,34,98,7,67]
a.sort()
b.sort()
c=[]
c.extend(a)
c.extend(b)
c.sort()
print (c)
print ("Question 6 STACK")
#Question 6 STACK
p=["Apple","Mango","Orange","Plum"]
print (p)
p.append("Banana")
print (p)
p.append("Blueberry")
print(p)
p.pop()
print (p)
p.pop()
print (p)
print ("Question 6 QUEUE")
#Question 6 QUEUE
p=["Apple","Mango","Orange","Plum"]
print (p)
p.append("Banana")
print (p)
p.append("Blueberry")
print (p)
p.pop(0)
print (p)
p.pop(0)
print (p)
print ("Optinal Question")
#Optional Question
k=[]
no=int(input("Enter total number of values: "))
for i in range(no):
    u=input("Enter a value ")
    k.append(u)
print (k)
e=0
o=0
for i in range(no):
    if(i%2==0):
        e=e+1
    else:
        o=o+1
print ("Number of even numbers are ",e)
print ("Number of odd numbers are ",o)
