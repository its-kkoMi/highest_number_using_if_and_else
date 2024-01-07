#Assignment 4
#Ask user to input 3 numbers.
#3Find and print the biggest number using only if-else statement

# - Import TK
import tkinter as tk
from tkinter import messagebox

# - GUI using Tk
app = tk.Tk()
app.title("Highest Number")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

# - Ask user to input three numbers
input_first_number = tk.Entry(frame)
input_first_number.grid(row=0, column=1)

input_second_number = tk.Entry(frame)
input_second_number.grid(row=1, column=1)

input_third_number = tk.Entry(frame)
input_third_number.grid(row=2, column=1)

# - Validate if the inputs are numeric
def validate_input():
    try:
        float(input_first_number.get())
        float(input_second_number.get())
        float(input_third_number.get())
        return True
    except ValueError:
        return False

# - Calculate using if-else the highest input
# - Make pop up messages for the highest input and error input
# - Entry Labels and Button
label_first_number = tk.Label(frame, text="Enter first number:")
label_first_number.grid(row=0, column=0)

label_second_number = tk.Label(frame, text="Enter second number:")
label_second_number.grid(row=1, column=0)

label_third_number = tk.Label(frame, text="Enter third number:")
label_third_number.grid(row=2, column=0)

button = tk.Button(frame, text="Find Highest")
button.grid(row=3, column=1)

# - Loop
app.mainloop()