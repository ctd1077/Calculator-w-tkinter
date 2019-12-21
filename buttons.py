# T&T/buttons.py

from tkinter import *

root = Tk()

def onClick():
    myLabel = Label(root, text='It Worked!')
    myLabel.pack()


myButton = Button(root, text='Start', command=onClick, bg='green', fg='white')
myButton.pack()

root.mainloop()


