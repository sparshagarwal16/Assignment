import tkinter
from tkinter import *
import tkinter as tk
#Question 1
print("Question 1")
r=Tk()
r.title('HEY')
z=Label(r,text="HELLO WORLD",width=15,height=5,bg="blue")
z.pack()
button=tk.Button(r, text='Exit',width=15,activebackground='red',activeforeground="black",bg="red",command=sys.exit)
button.pack()
#Question 2
print("Question 2")
def print1():
    s=Label(r,text="WELCOME",width=10,height=5,bg="white")
    s.pack(side=BOTTOM)
button2=tk.Button(r,text='Print',width=15, activebackground='black',activeforeground='white',bg='white',command=print1)
button2.pack()
#Question 3
print("Question 3")
def display():
    w.configure(text="HOW ARE YOU?")
    w.pack()
r=Tk()
p=Frame(r,bg='yellow')
w=Label(r,text='HEY',bg='green',width='15',height='15')
w.pack()
button2 = tk.Button(r, text='start', width=20, activebackground='#ccff00', activeforeground="white", bg="red",command=display)
button2.pack()
b = tk.Button(r, text='exit', width=20, activebackground='#ccff00', activeforeground="white", bg="blue", command=sys.exit)
b.pack()
#Question 4
print("Question 4")
root = Tk()
def returnEntry(arg=None):
    result = myEntry.get()
    resultLabel.config(text=result)
    myEntry.delete(0, END)
myEntry = Entry(root, width='20', bg="white")
myEntry.focus()
myEntry.bind("<Return>", returnEntry)
myEntry.pack()
enterEntry = Button(root, text="Print", command=returnEntry, width=20, bg="red")
enterEntry.pack()
resultLabel = Label(root, text="", bg="white")
resultLabel.pack()
root.mainloop()
