from tkinter import *

root  = Tk()

def myCLick():
    myLabel = Label(root, text="OK")
    myLabel.pack()

myButton = Button(root, text="Cancel", command=myCLick)
# myButton = Button(root, text="Cancel", command=myCLick, bg="#fff")
# myButton = Button(root, text="Cancel", command=myCLick, fg="green")
# myButton = Button(root, text="Cancel", state="DISABLED")
# myButton = Button(root, text="Cancel", padx=50, pady=50)
myButton.pack()

root.mainloop()