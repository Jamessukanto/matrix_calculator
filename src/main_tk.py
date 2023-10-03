import sys

import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as tkmacosx_button

from operators import RedirectPrintToTextWidget, operator_names
from utils.calculate import calculate
from utils.dialog import show_help_dialog


# tkinter ui
window = tk.Tk()
window.title("Not a Matrix Calculator")
window['bg']='black'

button_font = tk.font.Font(family="Helvetica", size=12, weight="bold")


# ui component - operator dropdown
dropdown_frame = tk.Frame(master=window, width=50, bg="black", height=50, pady=20) 
dropdown_frame.pack()

dropdown_label = tk.Label(
    dropdown_frame,
    text="Select an operation:",
    fg="light grey",
    bg="black",
    width=40,
    height=3,)
dropdown_label.pack()

dropdown_field = ttk.Combobox(
    dropdown_frame,
    values=operator_names,
    background="white",
    foreground="black",
    width=31,
    height=4,)
dropdown_field.set('matrix_info')  # default
dropdown_field.configure(height=20)
dropdown_field.pack()


# ui component - matrix input
mat_input_frame = tk.Frame(master=window, width=50, height=50, bg="black")
mat_input_frame.pack()

mat_input_label = tk.Label(
    mat_input_frame,
    text="Operand input(s):",
    fg="light grey",
    bg="black",
    width=40,
    height=3,)
mat_input_label.pack()

mat_input_textbox = tk.Text(
    mat_input_frame,
    height=5,
    width=43,)
mat_input_textbox.pack()

calculate_button = tkmacosx_button(
    mat_input_frame,
    text="CALCULATE",
    bg="blue",
    fg="white",
    width=312,
    height=40,
    borderless=1,
    font=button_font)
calculate_button.pack(pady=10)

help_button = tkmacosx_button(
    mat_input_frame,
    text="HELP",
    bg="black",
    fg="white",
    command=show_help_dialog,
    width=312,
    height=20,
    borderless=1,
    font=button_font)
help_button.pack()


# ui component - results 
result_frame = tk.Frame(master=window, width=50, height=50, bg="black", pady=10)
result_frame.pack()

result_label = tk.Label(
    mat_input_frame,
    text="Results:",
    fg="light grey",
    bg="black",
    width=40,
    height=3,)

result_scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL,)

result_textbox = tk.Text(
    result_frame,
    height=29,
    width=42, 
    state=tk.DISABLED,
    yscrollcommand=result_scrollbar.set,)

result_label.pack()
result_textbox.pack(side=tk.LEFT)
result_scrollbar.config(command=result_textbox.yview)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Set calculate as command
calculate_button.config(command=lambda: calculate(dropdown_field, mat_input_textbox, result_textbox))

# Redirect print to the result_textbox widget
sys.stdout = RedirectPrintToTextWidget(result_textbox)


window.mainloop()



