from ast import Lambda
from re import sub
from signal import signal
import tkinter as tk
from tkinter.ttk import LabelFrame
from turtle import bgcolor, color
import math
from unicodedata import decimal


root = tk.Tk()
root.title('Calculator')
root.geometry("300x430")
# root.configure(bg='#303030')

entry= tk.Entry(root, border=4)
entry.pack(padx=10, pady=10, fill=tk.X)


#(GRID)BUTTON FRAME INSIDE THE PACK WITH PRE-DEFINED WIDTH/HEIGHT OF BLOCKS 

buttonframe= tk.Frame(root, border=2, padx=5, pady=5)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)
buttonframe.pack(padx=3, pady=3, fill=tk.BOTH)


#functions for buttons defined below....

def clear():
    entry.delete(0,tk.END)


def click(number):
    current=str(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0, current+str(number))

#the conditional function statements for equal 

def equal():
    s_num=float(entry.get())
    entry.delete(0, tk.END)

    if to_do=='add':
        entry.insert(0, f_num + s_num)

    if to_do=='sub':
        entry.insert(0, f_num - s_num)

    if to_do=='multi':
        entry.insert(0, f_num * s_num)

    if to_do=='div':
        entry.insert(0, f_num / s_num)


#functions for buttons

def addition():
    global f_num
    global to_do
    to_do='add'
    f_num= float(entry.get())
    entry.delete(0, tk.END)

def subtraction():
    global f_num
    global to_do
    to_do='sub'
    f_num= float(entry.get())
    entry.delete(0, tk.END)

def multiplication():
    global f_num
    global to_do
    to_do='multi'
    f_num= float(entry.get())
    entry.delete(0, tk.END)

def division():
    global f_num
    global to_do
    to_do='div'
    f_num= float(entry.get())
    entry.delete(0, tk.END)

def square():
    global f_num
    global to_do
    to_do='square'
    f_num=float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, f_num * f_num)

def sqrt():
    global f_num
    global to_do
    to_do='sqrt'
    f_num=float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(f_num))

def logrithm():
    global f_num
    global to_do
    to_do='log'
    f_num=float(entry.get())
    entry.delete(0, tk.END)
    # if f_num==0:
    #     entry.insert(0, "Not Defined")
        
    # else:
    entry.insert(0, math.log(f_num))


def exp():
    global f_num
    global to_do
    entry.delete(0, tk.END)
    entry.insert(0, math.e)

def pie():
    global f_num
    global to_do
    entry.delete(0, tk.END)
    entry.insert(0, math.pi)

def delete():
    global f_num
    global to_do
    to_do='del'
    f_num=str(entry.get())
    entry.delete(0, tk.END)
    li=f_num.rstrip(f_num[-1])
    entry.insert(0, li)


#decimal function 

def point():
    # pass
    global f_num
    global to_do
    flag=0
    f_num=entry.get()
    for i in f_num:
        if i==".":
            flag=1
            break
    if flag==0:
        f_num=str(entry.get())
        dot="."
        entry.delete(0, tk.END)
        entry.insert(0,f_num+dot)



# functional buttons 

button_exp= tk.Button(buttonframe, text="e", padx=18, pady=18, command=exp)
button_exp.grid(row=0, column=0, sticky=tk.W+tk.E)

button_ce= tk.Button(buttonframe, text="pi", padx=20, pady=20, command=pie)
button_ce.grid(row=0, column=1, sticky=tk.W+tk.E)

button_c= tk.Button(buttonframe, text="CE", padx=20, pady=20, command=clear)
button_c.grid(row=0, column=2, sticky=tk.W+tk.E)

button_cross= tk.Button(buttonframe, text="Del", padx=20, pady=20, command=delete)
button_cross.grid(row=0, column=3, sticky=tk.W+tk.E)

buttonlnx= tk.Button(buttonframe, text="Lnx" ,  pady=20, command= logrithm)
buttonlnx.grid(row=1, column=0, sticky=tk.W+tk.E)

button_square= tk.Button(buttonframe, text="x^2", pady=20, command=square)
button_square.grid(row=1, column=1, sticky=tk.W+tk.E)

button_sqrt=tk.Button(buttonframe, text='x^0.5', pady=20, command=sqrt)
button_sqrt.grid(row=1, column=2, sticky=tk.W+tk.E)

button_point=tk.Button(buttonframe, text='.', pady=20, command=point)
button_point.grid(row=5, column=2, sticky=tk.W+tk.E)




#Buttons of numbers 

button1=tk.Button(buttonframe, text='1', pady=20, command=lambda: click(1))
button1.grid(row=4, column=0, sticky=tk.W+tk.E)

button2=tk.Button(buttonframe, text='2', pady=20, command=lambda: click(2))
button2.grid(row=4, column=1, sticky=tk.W+tk.E)

button3=tk.Button(buttonframe, text='3', pady=20, command=lambda: click(3))
button3.grid(row=4, column=2, sticky=tk.W+tk.E)

button4=tk.Button(buttonframe, text='4', pady=20, command=lambda: click(4))
button4.grid(row=3, column=0, sticky=tk.W+tk.E)

button5=tk.Button(buttonframe, text='5', pady=20, command=lambda: click(5))
button5.grid(row=3, column=1, sticky=tk.W+tk.E)

button6=tk.Button(buttonframe, text='6', pady=20, command=lambda: click(6))
button6.grid(row=3, column=2, sticky=tk.W+tk.E)

button7=tk.Button(buttonframe, text='7', pady=20, command=lambda: click(7))
button7.grid(row=2, column=0, sticky=tk.W+tk.E)

button8=tk.Button(buttonframe, text='8', pady=20, command=lambda: click(8))
button8.grid(row=2, column=1, sticky=tk.W+tk.E)

button9=tk.Button(buttonframe, text='9', pady=20, command=lambda: click(9))
button9.grid(row=2, column=2, sticky=tk.W+tk.E)

button0=tk.Button(buttonframe, text='0', pady=20, command=lambda: click(0))
button0.grid(row=5, column=1, sticky=tk.W+tk.E)

button_bracket=tk.Button(buttonframe, text='00', pady=20, command=lambda: click("00"))
button_bracket.grid(row=5, column=0, sticky=tk.W+tk.E)


#buttons for operators (+,-,/,x,=)


button_div=tk.Button(buttonframe, text='/', pady=20, command=division)
button_div.grid(row=1, column=3, sticky=tk.W+tk.E)

button_multi=tk.Button(buttonframe, text='X', pady=20, command=multiplication)
button_multi.grid(row=2, column=3, sticky=tk.W+tk.E)

button_sub=tk.Button(buttonframe, text='-', pady=20,command=subtraction)
button_sub.grid(row=3, column=3, sticky=tk.W+tk.E)

button_add=tk.Button(buttonframe, text='+', pady=20, command=addition)
button_add.grid(row=4, column=3, sticky=tk.W+tk.E)

button_equal=tk.Button(buttonframe, text='=', pady=20, bg='#91ffa7', command=equal)
button_equal.grid(row=5, column=3, sticky=tk.W+tk.E)


# execute the window
root.mainloop()
