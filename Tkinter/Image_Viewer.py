from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons, Images and Exit Buttons")
root.iconbitmap("python_original_logo.ico")


my_img1 = ImageTk.PhotoImage(Image.open("Images/logo1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/logo2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/logo3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/logo4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/logo5.png"))

images = [my_img1, my_img2, my_img3, my_img4, my_img5]



my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global btn_forward
    global btn_backward
    
    my_label.grid_forget()
    my_label = Label(image=images[image_number-1])
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    btn_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    
    if image_number == 5:
        btn_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    btn_backward.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

def backward(image_number):
    global my_label
    global btn_forward
    global btn_backward
    
    my_label.grid_forget()
    my_label = Label(image=images[image_number-1])
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    btn_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    
    if image_number == 1:
        btn_backward = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    btn_backward.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)
    
    


btn_backward = Button(root, text="<<", command=backward, state=DISABLED)
btn_close = Button(root, text="Close", width=50, command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_backward.grid(row=1, column=0)
btn_close.grid(row=1, column=1)
btn_forward.grid(row=1, column=2)


root.mainloop()