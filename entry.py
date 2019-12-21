# T&T/entry.py

from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='lightgrey')
e.pack()
e.insert(0, '$28,000')

def onClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text='Start', command=onClick, bg='green', fg='white')
myButton.pack()

root.mainloop()