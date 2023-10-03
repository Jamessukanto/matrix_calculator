import tkinter as tk


def show_help_dialog():
    help_text = """
    
    Thank you for using Not a Matrix Calculator!

    Hello, this app was developed by me, James, for offline
    matrix calculation during an exam.

    It's a work-in-progress, so if you encounter issues, or want
    to provide feedback, please don't hesitate to reach out! 
    I value your input and I'm at james.sukanto@gmail.com

    ---------------------------------------------------------------


    Constraints & known issues on inputting textbox operand(s):
    
    - Entry values cannot be fractions. Decimals are ok.

    - Vector in Rn is treated as a nx1 matrix for convenience 
        e.g. [2,3,4] is the same as [[2],[3],[4]] 

    - Having a space as your first character in the input
        invalidates your input! (I keep making this blunder too)
        Space between values is ok.

    - Pressing “ENTER” on keyboard marks a new operand. This is 
        handy for operations which require > 1 operand, namely:
        
        - matrix_multiply: Matrix and vector/matrix as input
        - dot: 2 vectors as input
        - orthonormalise_basis: multiple vectors as input

        
    ---------------------------------------------------------------


    User input examples:

        - matrix_info: 
            [[1, 2, 3], [4, 5, 6]] 
            “Click Calculate”

        - matrix_multiply: 
            [[1, 2], [3, 4]] “ENTER” [[1, 2], [3, 4]] “ENTER” [4, 4] 
            “Click Calculate”

        - dot: 
            [1, 1, 1] “ENTER” [2, 2, 2] 
            “Click Calculate”

        - diagonalise: 
            [[1, 2], [3, 4]] 
            “Click Calculate”

        - orthonormalise_basis: 
            [1, 1, 0] “ENTER” [0, 3, 2] “ENTER” [0, 5, 5] 
            “Click Calculate”

        - factorise_qr: 
            [[1, 2], [3, 4], [5, 6]] 
            “Click Calculate”

            
    
        
    """
    
    dialog = tk.Toplevel()
    dialog.title("Help")
    dialog.geometry("500x600")
    
    help_textbox = tk.Text(dialog, wrap=tk.WORD, width=80, height=70)
    help_textbox.insert(tk.END, help_text)
    help_textbox.pack()
    