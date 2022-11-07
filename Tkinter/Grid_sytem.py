from tkinter import *

root  = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Tkinter Learning Tool")
myLabel2 = Label(root, text="My name is Frank Patrick")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()