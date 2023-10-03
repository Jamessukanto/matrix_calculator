from operators.common import matrix_info, matrix_multiply, solve_augmented_matrix
from operators.inner_prod import euclidian_inner_product, orthonormalise_basis
from operators.factorise import factorise_qr, diagonalise


operators_map = {
    'matrix_info': [matrix_info, 'inf'],
    'matrix_multiply': [matrix_multiply, 'mul'],
    'dot': [euclidian_inner_product, 'dot'],
    # 'solve_augmented_matrix': [solve_augmented_matrix, 'sol],
    'diagonalise': [diagonalise, 'dia'],
    'orthonormalise_basis': [orthonormalise_basis, 'or'],
    'factorise_qr': [factorise_qr, 'qr'],
}

operator_names = [name for name in operators_map.keys()]
operator_initials = [item[1] for item in operators_map.values()]
operator_init_to_name = {init: name for init, name in zip(operator_initials, operator_names)}

class RedirectPrintToTextWidget(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Auto-scroll to the end of the text

def get_operator(operator):
    return operators_map[operator][0]