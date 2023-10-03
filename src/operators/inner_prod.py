from sympy import Matrix, pprint, GramSchmidt


def euclidian_inner_product(operands):
    print("EUCLIDIAN INNER PRODUCT: ")

    v1, v2 = Matrix(operands[0]), Matrix(operands[1])
    print("\nv1:")
    pprint(v1)
    print("\nv2:")
    pprint(v2)

    if len(operands) > 2:
        print("\Invalid input: There must be only 2 vectors")
        return
    if type(operands[0][0]) != int or type(operands[1][0]) != int:
        print("\nInvalid input: Only vectors are allowed for this operation")
        return
    
    print(f"\nDot product: {(v1.T * v2)[0]}")
    

def orthonormalise_basis(operands):
    print("ORTHONORMALISE WITH GRAM-SCHMIDT: ")

    print("\nu1 = v1")
    print("u2 = v2 - (<v2, u1> / <u1, u1>) * u1")
    print("u3 = v3 - (<v3, u1> / <u1, u1>) * u1 - (<v3, u2> / <u2, u2>) * u2")
    print("...")
    print("\nspan'{'u1,...,uk'}' == span'{'v1,...,vk'}'")

    vector_list = []
    vector_matrix = [[] for i in range(len(operands[0]))]

    for col in operands:
        vector_list.append(Matrix(col))
        for row_i, val in enumerate(col):
            vector_matrix[row_i].append(val)

    print("\nInput basis: ")
    pprint(vector_list)

    if type(operands[0][0]) != int:
        print("\nInvalid input: Only vectors are allowed for this operation")
        return

    basis_rank = Matrix(vector_matrix).rank()
    if len(operands) == basis_rank:
        print("\nGiven columns are linearly independent, all good.")
    else:
        print("\nGiven columns are NOT linearly independent. Rank is {basis_rank}. Remember to show reduction.")
    
    print("\nOrthogonal: ")
    pprint(GramSchmidt(vector_list))

    print("\nOrthonormal: ")
    pprint(GramSchmidt(vector_list, True))