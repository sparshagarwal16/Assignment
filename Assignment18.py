import tkinter
from tkinter import *
import tkinter as tk
#Question 1
print("Question 1")
dict={}
for i in range(2):
    name=input("Enter the name: ")
    mob=int(input("Enter mobile number: "))
    dict[name]=mob
r= Tk()
z=Label(r,text="DATA",width=15,bg="blue")
z.pack()
scrollbar = Scrollbar(r)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(r, yscrollcommand = scrollbar.set )
for line in dict:
    mylist.insert(END, str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
all_items=mylist.get(0,tkinter.END)
def poll():
    z.after(200, poll)
    sel = mylist.curselection()
    print(sel)
    if(len(sel)>0):
        t=all_items[sel[0]]
        z.config(text=dict[t])
poll()
print(all_items)
#Question 2
print("Question 2")
dict2={}
name1=""
name2=""
mob1=0
mob2=0
def add():
    name1=input("Enter the name: ")
    mob1=int(input("Enter mobile number: "))
    name2=input("Enter the name: ")
    mob2=int(input("Enter mobile number: "))
    dict2[name1]=mob1
    dict2[name2]=mob2
    print(dict2)
def insert():
    for line2 in dict2:     #entry added to GUI
        mylist.insert(END, str(line2))
    mylist.pack(side=LEFT, fill=BOTH)
button=tk.Button(r, text='ADD',width=15,activebackground='#1CDDD8',activeforeground="black",bg="#1CDDD8",command=add)
button.pack()
button2=tk.Button(r, text='Insert',width=15,activebackground='#1CDDD8',activeforeground="black",bg="#1CDDD8",command=insert)
button2.pack()
mainloop()