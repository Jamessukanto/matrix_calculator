from operators.lin_alg.common import matrix_info, matrix_multiply, solve_augmented_matrix
from operators.lin_alg.inner_prod import euclidian_inner_product, orthonormalise_basis
from operators.lin_alg.factorise import factorise_qr, diagonalise
from operators.stats.common import sample_info, binomial, negbinomial, poisson, exponential, normal, hypergeometric, uniform


operators_map = { # calculator: op_label: [op_func, op_initial]
    'stats': {
        'sample_info': [sample_info, 's_inf'],
        'b(k; n, p)': [binomial, 'sb'],
        'f(k; r, p)': [negbinomial, 'sf'],
        'p(k; p_mean)': [poisson, 'sp'],
        'e(k; lamb)': [exponential, 'se'],
        'n(k1, k2; p_mean, p_std)': [normal, 'sn'],
        'h(k, r=red_in_popn, h=sample_size, n=popn)': [hypergeometric, 'sh'],
        'uni': [uniform, 'su'],
    },
    'lin_alg': {
        'matrix_info': [matrix_info, 'la_inf'],
        'matrix_multiply': [matrix_multiply, 'la_mul'],
        'dot': [euclidian_inner_product, 'la_dot'],
        # 'solve_augmented_matrix': [solve_augmented_matrix, 'la_sol],
        'diagonalise': [diagonalise, 'la_dia'],
        'orthonormalise_basis': [orthonormalise_basis, 'la_or'],
        'factorise_qr': [factorise_qr, 'la_qr'],
    },
}

initial_to_operation = {}
for calc, op in operators_map.items():
    for op_label, (op_func, op_initial) in op.items():
        initial_to_operation[op_initial] = op_func