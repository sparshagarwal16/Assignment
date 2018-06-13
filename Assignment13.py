#Question 1
print("Question 1")
a=3
try:
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("The number is divided by zero")
#Question 2
print("Question 2")
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Out of index")
#Question 3
print("Question 3")
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
#Question 4
print("Question 4")
def AbyB(a,b):
    try:
        c =((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#Question 5
print("Question 5")
try:
    import hello
except ImportError:
    print("Import Error")
except ImportError:
    print("Import Error")
try:
    n=int(input("Enter a value: "))
    if(n<10):
        print(n)
    else:
        raise ValueError
except ValueError:
    print("Value Error")
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Out of index")
#Question 6
print("Question 6")
class AgeTooSmallError(Exception):
    pass
try:
    age=int(input("Enter age: "))
    if(age<18):
        raise AgeTooSmallError
    else:
        print("Age: ",age)
except AgeTooSmallError:
    print("Age too small")



