<br>

# Matrix Calculator for offline usage
I needed a matrix calculator for an exam, and accessing the internet is not allowed so, no Symbolab. Other students may not be familiar with CLI, hence, the UI.

__Features:__
- Matrix information on: RREF form (with steps to it), inverse form, null space
- Matrix multiplication
- Dot product
- Diagonalization (A=PDP**-1)
- Factorisation (QR)
- Orthonormalise basis

<br>

# Usage

First off, clone the repo to your local machine and navigate to the project directory. Install the app by navigating to `src` folder and running:

```
pyinstaller --onefile main_tk.py
```

That should generate a new folder `dist`. Double-click on `main_tk` within the new folder to run the app. 

<br>

![Group 4](https://github.com/Jamessukanto/matrix_calculator/assets/51419955/b2261b66-337c-4fae-ab42-b4b9d457142d)

<br>

Now, to run it on your terminal, you should first install the required packages from requirements.txt:

```
pip install -r requirements.txt
```

<br>

Great! Now, to see all the operations available run the command below. Each operation may require different inputs for its operands. 

```
python main_terminal.py help
```

<br>

## Example 1: Reduced row-echelon form (including steps)
Find out about the rref form, inverse, determinant, and null space of a given matrix. Note that 'inf' is the initial for the operation, and '[[1,2],[2,2]]' is the operand - I'm using bash so I need to wrap it with single quotation marks. 
```
python main_terminal.py inf '[[1,2],[2,2]]'
```

<br>

## Example 2: Orthonormalise a basis

Apply the Gram-Schmidt process to orthogonalise a set of vectors, then normalising them. Note that the input for this operation is a list of vectors, not a matrix. Here, 'or' is the operation initial and '[1,2]' '[2,2]' are the two operands.

```
python main_terminal.py or '[1,2]' '[2,2]' 
```

<br>
