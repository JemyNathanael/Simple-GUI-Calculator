import tkinter as tk # Import the library to make a GUI
import tkinter.messagebox
from tkinter import *

# make a window for our GUI
window = tk.Tk()
window.title("CALCULATOR-GUI") # add the GUI title
# window.geometry("800x800")

# make an Entry for user to do inputs in the calculator
entry = tk.Entry(master=window, background="skyblue", relief="sunken", width=60 )
entry.pack()

def click(nums):
    entry.insert(tk.END, nums) # insert number at the end of current content

def evaluateCalculation():
    try:
        x = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, x)
    except:
        tkinter.messagebox.showerror("Error", "Syntax error, please try again!")

def clearCalculator():
    entry.delete(0, tk.END)

def deleteNumbers():
    length = len(entry.get())
    entry.delete(len-1, 'end')

# Start creating the label for the results and buttons for user inputs
equation_txt = ""
equation_label = StringVar()
result_label = Label(master=window, textvariable=equation_label, width=50, height=2, bg="blue")
result_label.pack()

# make a frame for our buttons placement using grid 
frame = tk.Frame(master=window, background="black")
frame.pack(); 

# add the buttons
button_7 = tk.Button(master=frame, text="7", command=lambda: click(7),
                     padx=15, pady=7, width=3)
button_7.grid(row=1, column=0)

button_8 = tk.Button(master=frame, text="8", command=lambda: click(8),
                     padx=15, pady=7, width=3)
button_8.grid(row=1, column=1)

button_9 = tk.Button(master=frame, text="9", command=lambda: click(9),
                     padx=15, pady=7, width=3)
button_9.grid(row=1, column=2)

button_4 = tk.Button(master=frame, text="4", command=lambda: click(4),
                     padx=15, pady=7, width=3)
button_4.grid(row=2, column=0)

button_5 = tk.Button(master=frame, text="5", command=lambda: click(5),
                     padx=15, pady=7, width=3)
button_5.grid(row=2, column=1)

button_6 = tk.Button(master=frame, text="6", command=lambda: click(6),
                     padx=15, pady=7, width=3)
button_6.grid(row=2, column=2)

button_1 = tk.Button(master=frame, text="1", command=lambda: click(1),
                     padx=15, pady=7, width=3)
button_1.grid(row=3, column=0)

button_2 = tk.Button(master=frame, text="2", command=lambda: click(2),
                     padx=15, pady=7, width=3)
button_2.grid(row=3, column=1)

button_3 = tk.Button(master=frame, text="3", command=lambda: click(3),
                     padx=15, pady=7, width=3)
button_3.grid(row=3, column=2)

button_modulo = tk.Button(master=frame, text="%", command=lambda: click('%'),
                     padx=15, pady=7, width=3)
button_modulo.grid(row=4, column=0)

button_0 = tk.Button(master=frame, text="0", command=lambda: click(0),
                     padx=15, pady=7, width=3)
button_0.grid(row=4, column=1)

button_dot = tk.Button(master=frame, text=".", command=lambda: click('.'),
                     padx=15, pady=7, width=3)
button_dot.grid(row=4, column=2)

button_add = tk.Button(master=frame, text="+", command=lambda: click('+'),
                     padx=15, pady=7, width=3, foreground="green")
button_add.grid(row=2, column=3)

button_subtract = tk.Button(master=frame, text="-", command=lambda: click('+'),
                     padx=15, pady=7, width=3, foreground="green")
button_subtract.grid(row=2, column=3)

button_multiply = tk.Button(master=frame, text="x", command=lambda: click('*'),
                     padx=15, pady=7, width=3, foreground="green")
button_multiply.grid(row=0, column=2)

button_divide = tk.Button(master=frame, text="÷", command=lambda: click('/'),
                     padx=15, pady=7, width=3, foreground="green")
button_divide.grid(row=0, column=1)

button_clear = tk.Button(master=frame, text="C", command=clearCalculator(),
                     padx=15, pady=7, width=3, foreground="orange", background="black")
button_clear.grid(row=0, column=0)

window.mainloop()