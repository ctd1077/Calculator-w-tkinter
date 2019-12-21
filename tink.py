# T&T/tink.py

from tkinter import *

root = Tk()
root.title("T&T and BW Spreassheet Creator")

def myClick():
    myLabel = Label(root, text='Start')
    myLabel.pack()

l1 = Label(root, text="Truck Company")
l1.grid(row=0,column=0)

l2 = Label(root, text="Invoice Number")
l2.grid(row=1,column=0)

l3 = Label(root, text="Hot Oil:")
l3.grid(row=2,column=0)

l4 = Label(root, text="Water:")
l4.grid(row=2,column=1)

l5 = Label(root, text="Charges")
l5.grid(row=3,column=0)

l6 = Label(root, text="Hot Oil:") # Default $28,000
l6.grid(row=4,column=0)

l7 = Label(root, text="Water") # Default $11,000
l7.grid(row=4,column=1)

l8 = Label(root, text="Start Date:")
l8.grid(row=5,column=0)

l9 = Label(root, text="End Date:")
l9.grid(row=5,column=2)

root.mainloop()


