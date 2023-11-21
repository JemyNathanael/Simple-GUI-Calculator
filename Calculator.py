import tkinter as tk # Import the library to make a GUI
import tkinter.messagebox
from tkinter import *

# make a window for our GUI
window = tk.Tk()
window.title("CALCULATOR") # add the GUI title
window.geometry("800x800")

# make an Entry for user to do inputs in the calculator
entry = tk.Entry(master=window, background="skyblue", relief="sunken", width=60 )
entry.pack()

def click(nums):
    entry.insert(tk.END, nums) # intert number at the end of current content

def evaluateCalculation():
    try:
        x = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, x)
    except:
        tkinter.messagebox.showerror("Error", "Syntax error, please try again!")

def clearCalculator():
    entry.delete(0, tk.END)

# Start creating the label for the results and buttons for user inputs
equation_txt = ""
equation_label = StringVar()
result_label = Label(master=window, textvariable=equation_label, width=50, height=2, bg="blue")
result_label.pack()

# make a frame for our buttons placement using grid 
frame = tk.Frame(master=window)
frame.pack(); 

window.mainloop()