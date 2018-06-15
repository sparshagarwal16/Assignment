#Question 1
print("Question 1")
file=open('examle.txt','r')
l=file.readlines()
print(l)
print(len(l))
n=int(input("Enter the line number from last: "))
for i in range(len(l)-n,len(l)):
    print(l[i])
#Question 2
print("Question 2")
s=file.read()
d=s.split()
n=input("Enter the word to be counted: ")
if n in s:
    print(s.count(n))
#Question 3
print("Question 3")
a=''
a=file.read()
f=open('file1.txt','w')
f.write(a)
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()
file.close()
#Question 4
print("Question 4")
file=open("examle.txt","r")
f=open("file1.txt","r")
p=file.readlines()
t=file.readlines()
for i in range(len(p)):
    for j in range(len(t)):
        if(i==j):
            e=str(p[i])+str(t[j])
            print(e)
f.close()
file.close()
#Question 5
print("Question 5")
r=[]
p=open("Unsorted.txt","w")
f=open("sorted.txt","w")
import random
for i in range(0,10):
    t=random.randint(1,15)
    print(t)
    r.append(t)
print(r)
p.writelines(str(r))
p.close()
r.sort()
f.writelines(str(r))
f.close()
p=open("Unsorted.txt","r")
o=p.read()
print("unsorted file",o)
f.open("sorted.txt","r")
i=f.read()
print("sorted file",i)
