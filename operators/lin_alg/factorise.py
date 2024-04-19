from sympy import Matrix, pprint, shape, symbols, factor, expand


def factorise_qr(operands):
    print("QR FACTORISATION: ")

    A = Matrix(operands[0])
    print(f"\nA-matrix: '{operands[0]}'")
    pprint(A)

    if len(operands) != 1:
        print("\nInvalid input: There must be only 1 matrix")
        return
    if type(operands[0][0]) != list:
        print("\nInvalid input: Only m x n matrix is allowed for this operation. You've got a vector.")
        return
    
    A_rank = A.rank()    
    if len(operands[0][0]) != A_rank:
        print("\nGiven columns are NOT linearly independent. A cannot be factored as QR.")
        return

    print("\nGiven columns are linearly independent, all good.")
    print("\nNote that Q is orthonoramal <=> transpose(Q)*Q = I <=> R = transpose(Q)*A")
    Q, R = A.QRdecomposition()

    print(f"\nQ:       '{[list(Q.row(i)) for i in range(shape(Q)[0])]}'")
    pprint(Q)

    print(f"\nR:       '{[list(R.row(i)) for i in range(shape(R)[0])]}'")
    pprint(Q)


def diagonalise(operands):
    print("DIAGONALISE: ")

    A = Matrix(operands[0])
    print(f"\nA-matrix: '{operands[0]}'")
    pprint(A)

    lamda = symbols('lamda')
    polynomial = A.charpoly(lamda)
    print(f"\nChar polynomial:")
    factored = factor(polynomial.as_expr())
    pprint(expand(factored))
    pprint(factored)

    eigen = A.eigenvects()
    P = [[] for i in range(len(eigen[0][2][0]))]
    eigenvals = []
    
    for eigenval, multiplicity, eigenvectors in eigen:
        eigenvals.extend([eigenval for i in range(multiplicity)])

        eigenvect_pretty = Matrix(eigenvectors)
        for vector in eigenvectors:
            for i in range(len(P)):
                P[i].append(vector[i])
    
    print(f"\nP:        '{P}'")
    pprint(Matrix(P))

    D = Matrix.diag(eigenvals)
    print(f"\nD:        '{[list(D.row(i)) for i in range(shape(D)[0])]}'")
    pprint(D)

    if len(P[0]) != len(P):
        print(f"\nNot enough eigenvectors => not diagonalizable\n")
        return
    
    P_inv = Matrix(P)**-1
    print(f"\ninv(P):   '{[list(P_inv.row(i)) for i in range(shape(P_inv)[0])]}'")
    pprint(P_inv)