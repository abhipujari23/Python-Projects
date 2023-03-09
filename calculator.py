from tkinter import *
root = Tk()

val = Entry(root, width=45)
val.grid(row=0, column=0, columnspan=3)

def button_click(number):
    current = val.get()
    val.delete(0, END)
    val.insert(0, str(current) + str(number))

def func_add():
    first_num = int(val.get())
    global f_num 
    global math
    math = "add"
    f_num = int(first_num)
    val.delete(0, END)

def func_sub():
    first_num = int(val.get())
    global f_num 
    global math
    math = "sub"
    f_num = int(first_num)
    val.delete(0, END)

def func_mul():
    first_num = int(val.get())
    global f_num 
    global math
    math = "mul"
    f_num = int(first_num)
    val.delete(0, END)

def func_div():
    first_num = int(val.get())
    global f_num 
    global math
    math = "div"
    f_num = int(first_num)
    val.delete(0, END)

def func_equals():
    second_num = val.get()
    val.delete(0,END)
    if math == 'add':
        val.insert(0, f_num + int(second_num))
    elif math == 'sub':
        val.insert(0, f_num - int(second_num))
    elif math == 'div':
        val.insert(0, f_num / int(second_num))
    elif math == 'mul':
        val.insert(0, f_num * int(second_num))

#Number Buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text='+', padx=39, pady=20, command=func_add)
button_equal = Button(root, text='=', padx=86, pady=20, command=func_equals)
button_clear = Button(root, text='clear', padx=78, pady=20, command=lambda: val.delete(0, END))

button_sub = Button(root, text='-', padx=41, pady=20, command=func_sub)
button_mul = Button(root, text='*', padx=40, pady=20, command=func_mul)
button_div = Button(root, text='/', padx=40, pady=20, command=func_div)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=5, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6, column=2)

root.mainloop()