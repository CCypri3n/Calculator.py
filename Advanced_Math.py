from tkinter import *
import math
import pylab as pb
#creating the window
root = Tk()
#title of the window
root.title('Calculator')

e = Entry(root, width=15, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

pi = math.pi()
convert = pi/180

tan_txt = "tan"
sin_txt = "sin"
cos_txt = "cos"
atan = "f"
mode = "normal"

#function for Buttons.
def NumPad(nmb):
    global mode
    if mode == "graph":
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + (str(nmb))
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(nmb))
        print(current,nmb)
def button_clear():
    e.delete(0, END)
def button_add():
    global nmb1
    global mode
    if mode == "graph":
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + "+")
    else:
        nmb1 = int(e.get())
        e.delete(0, END)
        global factor
        factor = '+'
def button_substract():
    global nmb1
    global mode
    if mode == "graph":
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + "-")
    else:
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
    global ata   
    global factor
    factor = 'solo'
    nmb1 = int(e.get())
    ans = nmb1*convert
    if atan == 'f':
        ans = math.tan(ans)
    elif atan == 't':
        ans = math.atan(ans)
def button_sin():
    global nmb1
    global ans
    global atan
    global factor
    factor = 'solo'
    nmb1 = int(e.get())
    ans = nmb1*convert
    if atan == 'f':
        ans = math.sin(ans)
    elif atan == 't':
        ans = math.asin(ans)
def button_cos():
    global nmb1
    global ans
    global atan
    global factor
    factor = 'solo'
    nmb1 = int(e.get())
    ans = nmb1*convert
    if atan == 'f':
        ans = math.cos(ans)
    elif atan == 't':
        ans = math.acos(ans)
def button_graph:
    global mode
    e.delete(0, END)
    if mode == 'graph':
        mode = 'normal'
    else: 
        mode = 'graph'
def button_square():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str('**'))

def button_conv:
    global atan
    if atan == "f":
        atan == "t":
    else:
        atan = "f":
    button_txt("atan")
def txt(swap):
    if swap == "atan":
        if atan == "t":
            sin_txt = "asin"
            cos_txt = "acos"
            tan_txt = "atan"
        else:
            sin_txt = "sin"
            cos_txt = "cos"
            tan_txt = "tan"
def button_equal():
    if mode == 'normal':
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
        elif factor == 'solo':
            e.insert(0, ans)
    elif mode == 'graph':
        graph = e.get()
        pb.axis([-10, 10, -10, 10])
        pb.grid()
        x = pb.linspace(-10, 10, 100)
        y = int(graph)
        pb.plot(x, y)
        pb.show()
        
#Creating a Label (Text)
    
Button_1 = Button(root, text='1', padx=20,pady=20, command=lambda:NumPad(1)).grid(row=3, column=0)
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
Button_equal = Button(root, text='=', padx=20,pady=20, command=button_equal, ).grid(row=5, column=0)
Button_clear = Button(root, text='c', padx=50,pady=20, command=button_clear, ).grid(row=5, column=1)
Button_tan = Button(root, text=tan_txt, padx=20,pady=20, command=button_tan, ).grid(row=6, column=0)
Button_sin = Button(root, text=sin_txt, padx=20,pady=20, command=button_sin, ).grid(row=6, column=1)
Button_cos = Button(root, text=cos_txt, padx=20,pady=20, command=button_cos, ).grid(row=6, column=2)
Button_conv = Button(root, text='^-1', padx=20,pady=20, command=button_conv, ).grid(row=6, column=3)
Button_graph = Button(root, text='graph', padx=50,pady=20, command=button_graph, ).grid(row=6, column=4)
Button_square = Button(root, text='^', padx=50,pady=20, command=button_square, ).grid(row=6, column=5)

root.mainloop()
