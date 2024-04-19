import sys

import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as tkmacosx_button

from operators import operators_map
from ui_update import RedirectPrintToTextWidget
from ui_update.calculate import calculate
from ui_update.help_dialog import show_help_dialog


def update_op_dropdown(event):
    ops = list(operators_map[calc_dropdown_field.get()].keys())
    op_dropdown_field['values'] = ops
    op_dropdown_field.set(ops[0])

calcs = list(operators_map.keys())
ops = list(operators_map[calcs[0]].keys())


window = tk.Tk()
window.title("Solvero")
button_font = tk.font.Font(family="Helvetica", size=12, weight="bold")
col_button = "blue"
col_bg = window['bg'] = "black"
col_fg = "white"


# ui - operator selection
op_frame = tk.Frame(
    master=window, width=50, bg=col_bg, height=40, pady=20,) 

calc_dropdown_field = ttk.Combobox(
    op_frame, values=calcs,
    background=col_fg, foreground=col_bg, width=31, height=30,)

op_dropdown_field = ttk.Combobox(
    op_frame, values=ops,
    background=col_fg, foreground=col_bg, width=31, height=20,)

calc_dropdown_field.set(calcs[0])
calc_dropdown_field.pack()
op_frame.pack()
op_dropdown_field.set(ops[0])
op_dropdown_field.pack()
op_dropdown_field.pack(pady=10)
calc_dropdown_field.bind("<<ComboboxSelected>>", update_op_dropdown)


# ui - text input
input_frame = tk.Frame(
    master=window, width=50, height=50, bg=col_bg)

input_label = tk.Label(
    input_frame, text="Operand input(s):",
    bg=col_bg, fg="light grey", width=40, height=3,)

input_textbox = tk.Text(
    input_frame, height=5, width=43,)

calculate_button = tkmacosx_button(
    input_frame, text="CALCULATE",
    bg=col_button, fg=col_fg, width=312, height=40, borderless=1, font=button_font)

help_button = tkmacosx_button(
    input_frame, text="HELP", command=show_help_dialog, 
    bg=col_bg, fg=col_fg, width=312, height=20, borderless=1, font=button_font)

input_frame.pack()
input_label.pack()
input_textbox.pack()
calculate_button.pack()
calculate_button.pack(pady=10)
help_button.pack()
calculate_button.config(command = lambda: calculate(
    calc_dropdown_field, op_dropdown_field, input_textbox, result_textbox))


# ui - results 
result_frame = tk.Frame(
    master=window, width=50, height=50, bg=col_bg, pady=10)

result_label = tk.Label(
    input_frame, text="Results:",
    fg="light grey", bg=col_bg, width=40, height=3,)

result_scrollbar = ttk.Scrollbar(
    result_frame, orient=tk.VERTICAL,)

result_textbox = tk.Text(
    result_frame,
    height=29, width=42, state=tk.DISABLED, yscrollcommand=result_scrollbar.set,)

result_frame.pack()
result_label.pack()
result_textbox.pack(side=tk.LEFT)
result_scrollbar.config(command=result_textbox.yview)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Redirect print to the result_textbox widget
sys.stdout = RedirectPrintToTextWidget(result_textbox)

window.mainloop()