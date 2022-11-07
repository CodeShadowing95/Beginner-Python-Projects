from tkinter import *

root  = Tk()

e = Entry(root, width=50)
# e = Entry(root, borderwidth=5)
# e = Entry(root, bg="#000", fg="#fff")
# e = Entry(root, width=50)
e.pack()
# e.insert(0, "Enter your name(default value)")

def myCLick():
    hello = "Welcome to Tkinter, " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="OK", command=myCLick)
myButton.pack()

root.mainloop()