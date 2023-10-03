from sympy import Matrix, pprint, shape


def solve_augmented_matrix(operands):
    print("SOLVE AUGMENTED MATRIX: ")

    A = Matrix(operands[0])
    print(f"\nA-matrix: '{operands[0]}'")
    pprint(A)

    b = Matrix(operands[1])
    print(f"\nb:        '{operands[1]}'")
    pprint(b)

    if len(operands) != 2:
        print("\nInvalid input: There must be 1 matrix and 1 vector")
        return
    
    if type(operands[1][0]) != int:
        print("\nInvalid input: b must be an appropriate vector")
        return
    
    Ab = A.row_join(b)
    print("\nAb:")
    pprint(Ab)
    
    # rref
    Ab_rref, _ = Ab.rref()
    print(f"\nrref(augmented_matrix):")
    pprint(Ab_rref)

    print("""\nNotes:
Free var <=> Ax=b has infinite solutions <=> not one-to-one/injective <=> A is lin dep
\nHas zero-row (not counting b) <=> not onto/surjective\n""")


def matrix_multiply(operands):
    print("MATRIX MULTIPLICATION: ")

    A = Matrix(operands[0])
    print(f"\nA-matrix: '{operands[0]}'")
    pprint(A)

    for operand in operands[1:]:
        print(f"\nOperand:  '{operand}'")
        pprint(Matrix(operand))
        A = A * Matrix(operand)

    print(f"\nResult:   '{[[float(v) for v in A.row(i)] for i in range(shape(A)[0])]}'")
    pprint(A)


def matrix_info(operands):
    print("MATRIX INFO: ")

    A = Matrix(operands[0])
    print(f"\nA-matrix: '{operands[0]}'")
    pprint(A)
    
    if len(operands) != 1:
        print("\nInvalid input: There must be only 1 matrix")
        return
    
    # rref
    A_rref, _ = A.rref()
    print(f"\nRREF:     '{[list(A_rref.row(i)) for i in range(shape(A_rref)[0])]}'")
    pprint(A_rref)

    # null space
    A_null = A.nullspace()
    print(f"\nNull space:")
    pprint(A_null)

    # inverse
    if shape(A)[0] == shape(A)[1]:
        det = A.det()
        if det == 0:
            print(f"\ndet(A):    {det}, not invertible")
        else:
            print(f"\ndet(A):    {det}, invertible")
            A_inv = Matrix(A**-1)
            print(f"\ninv(A):    '{[[float(v) for v in A_inv.row(i)] for i in range(shape(A_inv)[0])]}'")                            
            pprint(A_inv)
    else:
        print("\nMatrix-A is not square -> no det(A)\n")        
        
    print("\n\n\n_________________________________________")  # [[1,2,3,4],[5,6,7,8],[2,2,4,4],[3,1,3,0]]


    # display steps of row reduction

    print("\nIntermediate Steps:\n\n")
    print("\nStep 0:")
    A_copy = A.copy()
    pprint(A_copy)

    num_rows, num_cols = A_copy.shape
    for pivot_row in range(min(num_rows, num_cols)): 
        print(f"\nStep {pivot_row + 1}:")

        # Scale the pivot row to have a leading 1
        leading_entry = A_copy[pivot_row, pivot_row]
        if leading_entry != 0:
            A_copy[pivot_row, pivot_row:] /= leading_entry
            print(f"Row {pivot_row + 1} = Row {pivot_row + 1} / ({leading_entry})")

        for row in range(num_rows):
            if row != pivot_row:
                # Subtract multiples of the pivot row from other rows
                multiplier = A_copy[row, pivot_row]
                if multiplier == 0:
                    continue
                A_copy[row, pivot_row:] -= multiplier * A_copy[pivot_row, pivot_row:]
                print(f"Row {row + 1} = Row {row + 1} - ({multiplier} * Row {pivot_row + 1})")
        pprint(A_copy, use_unicode=True)  # Pretty print the matrix

    # Now A_copy contains the reduced row-echelon form (rref)
    print(f"\n\nRREF:     '{[list(A_rref.row(i)) for i in range(shape(A_rref)[0])]}'")
    pprint(A_rref)

    print("\n\n_________________________________________")
    print("""\nGeneric notes on inference:
\nFree var <=> Ax=b has infinite solutions <=> not one-to-one/injective <=> A is lin dep
\nHas zero-row (not counting b) <=> not onto/surjective""")
    print("\n_________________________________________\n\n")