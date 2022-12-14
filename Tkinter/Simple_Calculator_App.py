from tkinter import *

root  = Tk()
root.title("Simple Calculator App")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(n):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n))

def button_clear():
    e.delete(0, END)

def button_add():
    n1 = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(n1)
    e.delete(0, END)

def button_subtract():
    n1 = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(n1)
    e.delete(0, END)

def button_multiply():
    n1 = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(n1)
    e.delete(0, END)

def button_divide():
    n1 = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(n1)
    e.delete(0, END)

def button_equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(n2))
    if math == "subtraction":
        e.insert(0, f_num - int(n2))
    if math == "multiplication":
        e.insert(0, f_num * int(n2))
    if math == "division":
        e.insert(0, f_num / int(n2))


# define buttons
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
btn_add = Button(root, text="+", padx=39, pady=20, command=button_add)
btn_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
btn_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

btn_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
btn_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply)
btn_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)



# Display buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_add.grid(row=5, column=0)
btn_equal.grid(row=5, column=1, columnspan=2)

btn_subtract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)

root.mainloop()