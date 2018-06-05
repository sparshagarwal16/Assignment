print("Question 1")
#Question 1
for i in range(10):
    num=int(input("Enter a number: "))
    print("The input number is ",num)
print("Question 2")
#Question 2
i=1
while True:
    print(i)
    i+=1
    if(i==5):
     break
print("Question 3")
#Question 3
no=int(input("Enter total number of integers: "))
imp=[]
for i in range(no):
    ip = int(input("Enter an integer:"))
    imp.append(ip)
print("Input List")
print(imp)
u=[]
for i in imp:
    u.append(i*i)
print("Squared List")
print(u)
print("Question 4")
#Question 4
a=[4,56,"Apple","Mango",4.8,3.5]
it=[]
st=[]
f=[]
for i in a:
    if(type(i)==int):
        it.append(i)
    elif(type(i)==str):
        st.append(i)
    else:
        f.append(i)
print("Original List: ",a)
print("Integer List: ",it)
print("String List: ",st)
print("Float List: ",f)
print("Question 5")
#Question 5
l=[]
for i in range(1,101):
    count=0
    if(i==1):
        continue
    else:
     for k in range(2,i//2+1):
        if(i%k==0):
         count=count+1
     if(count==0):
      l.append(i)
print("List of Prime Numbers: ",l)
print("Question 6")
#Question 6
for i in range(5):
    print("*"*i)
print("Question 7")
#Question 7
dict={}
for d in range(2):
    fruit_name= input("Enter name of the fruit ")
    q=int(input("Enter quantity "))
    dict[fruit_name]=q
print(dict)
print("Question 8")
#Question 8
li=[]
no=int(input("Enter total number of elements: "))
for i in range(no):
    u=input("Enter a value: ")
    li.append(u)
d=input("Enter the element to be deleted: ")
for i in li:
    if(i==d):
        li.remove(d)
    else:
        print("Input element not present")
print(li)






