from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons, Images and Exit Buttons")
root.iconbitmap("python_original_logo.ico")


my_img = ImageTk.PhotoImage(Image.open("python_logo1.png"))
my_label = Label(image=my_img)
my_label.pack()



btn_quit = Button(root, text="Exit Program", command=root.quit)
root.mainloop()