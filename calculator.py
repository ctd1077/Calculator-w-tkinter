# Calculator/calculator.py

from tkinter import *

root = Tk()
root.title('Simple Calculator')
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def onClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

def button_add():
    return

# Define Buttons

button_1 = Button(root, text='1', command=button_add, padx=40, pady=20)
button_2 = Button(root, text='2', command=button_add, padx=40, pady=20)
button_3 = Button(root, text='3', command=button_add, padx=40, pady=20)
button_4 = Button(root, text='4', command=button_add, padx=40, pady=20)
button_5 = Button(root, text='5', command=button_add, padx=40, pady=20)
button_6 = Button(root, text='6', command=button_add, padx=40, pady=20)
button_7 = Button(root, text='7', command=button_add, padx=40, pady=20)
button_8 = Button(root, text='8', command=button_add, padx=40, pady=20)
button_9 = Button(root, text='9', command=button_add, padx=40, pady=20)
button_0 = Button(root, text='0', command=button_add, padx=40, pady=20)

button_add = Button(root, text='+', command=button_add, padx=40, pady=20)
button_clear = Button(root, text='C', command=button_add, padx=40, pady=20)
button_equal = Button(root, text='=', command=button_add, padx=90, pady=20)



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

button_0.grid(row=4, column=1)

button_clear.grid(row=4, column=0)
button_add.grid(row=4, column=2)
button_equal.grid(row=5, column=0, columnspan=3)

root.mainloop()