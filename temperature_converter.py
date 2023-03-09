from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(False, False)

def convert():
    val = float(temperature_value.get())
    op = var.get()
    if op == 1:
        temp = (val * (9/5)) + 32

    elif op == 2:
        temp = (val - 32) * (5/9)
    temp_label = Label(root, text="{} Celcius is {} Farenheit".format(val, temp))
    temp_label.grid(row=3, column=0)

label = Label(root, text="Enter Temperature: ")
temperature_value = Entry(root)
submit = Button(root, text="Submit", command=convert)

var = IntVar()
cel_to_faren = Radiobutton(root, text="Celcius to Farenheit", variable=var, value=1)
faren_to_cel = Radiobutton(root, text="faren_to_cel", variable=var, value=2)

label.grid(row=0, column=0)
temperature_value.grid(row=0, column=1)
cel_to_faren.grid(row=1, column=0)
faren_to_cel.grid(row=1, column=1)
submit.grid(row=2, column=0, columnspan=2)


mainloop()