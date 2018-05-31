print("TUPLE")
print("Question 1")
#TUPLE
#Question 1
t=(2,5,"Apple","Google")
print(t)
print(len(t))
print("Question 2")
#Question 2
x=(2,3,56,48)
y=("Apple","Google","Microsoft","Adobe")
print(max(x))
print(min(x))
print(max(y))
print(min(y))
print("Question 3")
#Question 3
z=1
for i in x:
    z=z*i
print("Product of the elements of the Tuple are ",z)
print("SETS")
print("Question 1")
#SETS
#Question 1
print("First set")
s=set()
n=int(input("Enter total number of elements "))
for f in range(n):
     s1=input("Enter a value ")
     s.add(s1)
print(s)
print("Second set")
w=set()
e=int(input("Enter total number of elements "))
for f in range(e):
    w1=input("Enter a value ")
    w.add(w1)
print(w)
r=s-w
print("Difference: ",r)
q=s<=w
print("Comaprision: ",q)
z=s>=w
print("Comparsion: ",z)
print("Intersection: ",s&w)
print("Dictionaries")
print("Question 1")
#Dictionaries
#Question 1
dict={}
for l in range(2):
    student_name= input("Enter name of the student ")
    marks=int(input("Enter marks of the student "))
    dict[student_name]=marks
print(dict)
print("Question 2")
#Question 2
s=sorted(dict.items(),key=lambda t:t[1])
print(s)
print("Question 3")
#Question 3
s="MISSISSIPPI"
d={}
d["M"]=s.count("M")
d["I"]=s.count("I")
d["S"]=s.count("S")
d["P"]=s.count("P")
print(d)