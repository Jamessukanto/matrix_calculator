import sys
from io import StringIO
import ast

import tkinter as tk
from tkinter import messagebox

from operators import get_operator
    

def calculate(dropdown_field, mat_input_textbox, result_textbox):
    operator = dropdown_field.get()

    try:
        input_text = mat_input_textbox.get("1.0", "end-1c")
        input_lines = input_text.split('\n')

        # Evaluate each line separately to get a list of matrices
        operands = [ast.literal_eval(line) for line in input_lines if line.strip()]

        # Redirect print to the Text widget
        output_text = StringIO()
        sys.stdout = output_text
        
        get_operator(operator)(operands)

        # Retrieve the printed output
        output = output_text.getvalue()

        # Display the output in the Text widget
        result_textbox.config(state=tk.NORMAL)  # Enable text widget for editing
        result_textbox.delete("1.0", tk.END)  # Clear previous results
        result_textbox.insert("1.0", output)  # Insert new output
        result_textbox.config(state=tk.DISABLED)  # Disable text widget for editing

    except (ValueError, SyntaxError) as e:
        messagebox.showerror("Error", f"Invalid input. {str(e)}")