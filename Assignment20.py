#Question 1
print("Question 1")
import pandas as pd
import numpy as np
data={'Name':['Tom'],'Age':[19],'Mail ID':['tom@hotmail.com'],'Phone Number':[9897213461]}
df=pd.DataFrame(data)
df.loc[1]=[18,'marc@hotmail.com','Marc',8725214631]
print(df)
#Question 2
print("Question 2")
d=pd.read_csv('Sample.csv')
print(d)
#(a)
print("(a)")
print(d.head(5))
#(b)
print("(b)")
print(d.head(10))
#(c)
print("(c)")
print(d['MinTemp'].mean())
#(d)
print("(d)")
print(d.tail(5))
#(e)
print("(e)")
print(d['MaxTemp'].mean())
print(d['Rainfall'].sum())

