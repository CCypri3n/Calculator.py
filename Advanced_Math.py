from tkinter import *
import math
#creating the window
root = Tk()
#title of the window
root.title('Calculator')

e = Entry(root, width=15, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

pi = math.pi()
tangens = pi/180

#function for Buttons.
def NumPad(nmb):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nmb))
    print(current,nmb)
def button_clear():
    e.delete(0, END)
def button_add():
    global nmb1
    nmb1 = int(e.get())
    e.delete(0, END)
    global factor
    factor = '+'
def button_substract():
    global nmb1
    nmb1 = int(e.get())
    e.delete(0, END)
    global factor
    factor = '-'
def button_multiply():
    global nmb1
    nmb1 = int(e.get())
    e.delete(0, END)
    global factor
    factor = '*'
def button_divide():
    global nmb1
    nmb1 = int(e.get())
    e.delete(0, END)
    global factor
    factor = '/'
def button_tan():
    global nmb1
    global ans
    nmb1 = int(e.get())
    ans = nmb1*tangens
def button_equal():
    global nmb2
    nmb2 = int(e.get())
    e.delete(0, END)
    global ans
    if factor == '+':
        ans = nmb1+nmb2
        e.insert(0, ans)
    elif factor == '-':
        ans = nmb1-nmb2
        e.insert(0, ans)
    elif factor == '*':
        ans = nmb1*nmb2
        e.insert(0, ans)
    elif factor == '/':
        ans = nmb1/nmb2
        e.insert(0, ans)
    elif factor == 'tan':
        e.insert(0, ans)
#Creating a Label (Text)
    
Button_1 = Button(root, text='1', padx=20,pady=20, command=lambda:NumPad(1), fg='#f01f01').grid(row=3, column=0)
Button_2 = Button(root, text='2', padx=20,pady=20, command=lambda:NumPad(2)).grid(row=3, column=1)
Button_3 = Button(root, text='3', padx=20,pady=20, command=lambda:NumPad(3)).grid(row=3, column=2)
Button_4 = Button(root, text='4', padx=20,pady=20, command=lambda:NumPad(4)).grid(row=2, column=0)
Button_5 = Button(root, text='5', padx=20,pady=20, command=lambda:NumPad(5)).grid(row=2, column=1)
Button_6 = Button(root, text='6', padx=20,pady=20, command=lambda:NumPad(6)).grid(row=2, column=2)
Button_7 = Button(root, text='7', padx=20,pady=20, command=lambda:NumPad(7)).grid(row=1, column=0)
Button_8 = Button(root, text='8', padx=20,pady=20, command=lambda:NumPad(8)).grid(row=1, column=1)
Button_9 = Button(root, text='9', padx=20,pady=20, command=lambda:NumPad(9)).grid(row=1, column=2)
Button_0 = Button(root, text='0', padx=20,pady=20, command=lambda:NumPad(0)).grid(row=4, column=0)
Button_add = Button(root, text='+', padx=20,pady=20, command=button_add).grid(row=4, column=1)
Button_substract = Button(root, text='-', padx=21,pady=20, command=button_substract).grid(row=4, column=2)
Button_multiply = Button(root, text='*', padx=21,pady=20, command=button_multiply).grid(row=4, column=3)
Button_divide = Button(root, text='/', padx=21,pady=20, command=button_divide).grid(row=4, column=4)
Button_equal = Button(root, text='=', padx=20,pady=20, command=button_equal, ).grid(row=5, column=0,)
Button_clear = Button(root, text='c', padx=50,pady=20, command=button_clear, ).grid(row=5, column=1, columnspan=2)
Button_tan = Button(root, text='tan', padx=20,pady=20, command=button_tan, ).grid(row=6, column=0, columnspan=2)
root.mainloop()
