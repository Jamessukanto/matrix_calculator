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
You can download the app at `dist/main_tk` and install it locally. 

<br>

![Group 4](https://github.com/Jamessukanto/matrix_calculator/assets/51419955/b2261b66-337c-4fae-ab42-b4b9d457142d)

<br>

Or, you could interface on CLI. To do so, clone the repo to your local machine and navigate to the project directory. Install the required packages from requirements.txt:
create a new environment:
```
pip install -r requirements.txt
```
To run the project, navigate to src folder and use the following command:

```
python main_terminal.py help
```
<br>

That should list the operations enabled. Each operation may require different inputs for its operands. 

<br>

## Example 1: Reduced row-echelon form (including steps)
For instance, to find out about the rref form, inverse, determinant, and null space of a matrix, run: 
```
python main_terminal.py inf '[[1,2],[2,2]]'
```
Note that 'inf' is the initial for the operation, and '[[1,2],[2,2]]' is the operand (I'm using bash so I need to wrap it with single quotation marks). 

<br>

## Example 2: Orthonormalise a basis

Note that the input for this operation is a list of vectors, not a matrix. Here, 'or' is the operation initial and '[1,2]' '[2,2]' are the two operands. Simply run:

```
python main_terminal.py or '[1,2]' '[2,2]' 
```

<br>
