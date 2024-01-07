#Assignment 4
#Ask user to input 3 numbers.
#3Find and print the biggest number using only if-else statement

# - Import TK
import tkinter as tk
from tkinter import messagebox

# - GUI using Tk
app = tk.Tk()
app.title("Maximum Number Finder")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# - Ask user to input three numbers
# - Validate if the inputs are numeric
# - Calculate using if-else the highest input
# - Make pop up messages for the highest input and error input
# - Labels and Buttonsb