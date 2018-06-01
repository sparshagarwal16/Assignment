print("Question 1")
#Question 1
y=int(input("Enter the year: "))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("The input year is a leap year")
        else:
            print("The input year is not a leap year")
    else:
        print("The input year is a leap year")
else:
    print("The input year is not a leap year")
print("Question 2")
#Question 2
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
if(l==b):
    print("The entered dimensions are of a square")
else:
    print("The entered dimensions are of a rectangle")
print("Question 3")
#Question 3
a1=int(input("Enter the age of the first person: "))
a2=int(input("Enter the age of the second person: "))
a3=int(input("Enter the age of the third person: "))
if(a1>a2) and (a2>a3):
        print("First person is the oldest")
        print("Third person is the youngest")
if(a1>a3) and (a3>a2):
        print("First person is the oldest")
        print("Second person is the youngest")
if(a2>a3) and (a3>a1):
    print("Second person is the oldest")
    print("First person is the youngest")
if(a2>a1) and (a1>a3):
        print("Second person is the oldest")
        print("Third person is the youngest")
if(a3>a1) and (a1>a2):
        print("Third person is the oldest")
        print("Second person is the youngest")
if(a3>a2) and (a2>a1):
        print("Third person is the oldest")
        print("First person is the youngest")
print("Question 4")
#Question 4
age=int(input("Enter the age: "))
if(age>=20) and (age<=60):
    s=input("Enter sex - Press 'M' for Male and Press 'F' for Female: ")
    ms=input("Enter marital status - Press 'Y' for married and Press 'N' for unmarried: ")
    if(s=='F'):
        print("You may work only in urban areas")
    if(s=='M'):
        if(age>=20) and(age<40):
         print("You may work anywhere")
        if(age>=40) and (age<=60):
         print("You may work only in urban areas")
else:
    print("ERROR")
print("Question 5")
#Question 5
q=int(input("Enter quantity"))
if(q>1000):
    print("Discount Applicable")
    cost=100*q
    discost=cost-(cost*0.1)
    print("Total amount is ",cost)
    print("Amount after discount is ",discost)
else:
    print("Discount Not Applicable")


