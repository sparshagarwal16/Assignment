#Question 1
print("Question 1")
import numpy as np
a = np.random.rand(10,1)
print(a)
print("Mean of elements: ",np.mean(a))
#Question 2
print("Question 2")
b=np.random.rand(20,1)
print(b)
print("Variance: ",b.var())
print("Standard Deviation: ",b.std())
#Question 3
print("Question 3")
A=np.random.rand(10,20)
B=np.random.rand(20,25)
C=A.dot(B)
print("Multiplcation of Matrix A and Matrix B:\n",C)
print("Sum of elements: ",np.sum(C))
#Question 4
print("Question 4")
A=np.random.rand(10,1)
print("Original Array: \n",A)
def func(x):
    return(1/(1+np.exp(-x)))
final= np.apply_along_axis(func,0,A)
print("New Array: \n",final)



