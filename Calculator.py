import tkinter as tk # Import the library to make a GUI
import tkinter.messagebox
# from tkinter.constants import SUNKEN 

# make a window for our GUI
window = tk.Tk()
window.title("CALCULATOR") # add the GUI title

# make a frame to contains our previous window
frame = tk.Frame(master=window, background="blue", cursor="heart", highlightcolor="yellow")
frame.pack(); # pack the frame
# make an Entry for user to do inputs in the calculator
entry = tk.Entry(master=frame, background="red", highlightcolor="orange", relief="sunken", width=40, borderwidth=4)
entry.grid(column=0, row=0)

def click(nums):
    entry.insert(tk.END, nums) # intert number at the end of current content

