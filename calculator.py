# Calculator/calculator.py

from tkinter import *

root = Tk()
root.title('Simple Calculator')
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def onClick(number):
    current = e.get() # First save the current number displayed
    e.delete(0, END) # Next delete the current number displayed
    e.insert(0, str(current) + str(number)) # Make sure the 

def onClear():
    e.delete(0,END)

def onAdd():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0,END)

def onPercent():
    return

def onSubtract():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0,END)

def onMultiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0,END)

def onDivide():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0,END)

def onEqual():
    second = int(e.get())
    e.delete(0,END)

    if math == 'addition':
        e.insert(0, f_num + second)
    elif math == 'subtraction':
        e.insert(0, f_num - second)
    elif math == 'multiplication':
        e.insert(0, f_num * second)
    elif math == 'division':
        e.insert(0, f_num / second)



# Define Buttons
button_1 = Button(root, text='1', command=lambda: onClick(1), padx=40, pady=20)
button_2 = Button(root, text='2', command=lambda: onClick(2), padx=40, pady=20)
button_3 = Button(root, text='3', command=lambda: onClick(3), padx=40, pady=20)
button_4 = Button(root, text='4', command=lambda: onClick(4), padx=40, pady=20)
button_5 = Button(root, text='5', command=lambda: onClick(5), padx=40, pady=20)
button_6 = Button(root, text='6', command=lambda: onClick(6), padx=40, pady=20)
button_7 = Button(root, text='7', command=lambda: onClick(7), padx=40, pady=20)
button_8 = Button(root, text='8', command=lambda: onClick(8), padx=40, pady=20)
button_9 = Button(root, text='9', command=lambda: onClick(9), padx=40, pady=20)
button_0 = Button(root, text='0', command=lambda: onClick(0), padx=40, pady=20)

button_clear = Button(root, text='C', command=onClear, padx=40, pady=20) # lambda not needed here
button_equal = Button(root, text='=', command=lambda: onEqual(), padx=90, pady=20)
button_percent = Button(root, text='/', command=lambda: onPercent(), padx=40, pady=20)

button_add = Button(root, text='+', command=lambda: onAdd(), padx=40, pady=20)
button_subtract = Button(root, text='-', command=lambda: onSubtract(), padx=40, pady=20)
button_multiply = Button(root, text='*', command=lambda: onMultiply(), padx=40, pady=20)
button_divide = Button(root, text='/', command=lambda: onDivide(), padx=40, pady=20)


# Add the button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_percent.grid(row=4, column=2)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=5)

root.mainloop()