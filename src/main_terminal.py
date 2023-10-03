import sys
import argparse
import ast

from operators import get_operator, operator_init_to_name


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="arg parser")
    parser.add_argument("operator", type=str, help="Operator to perform")
    parser.add_argument("operands", type=str, nargs="*", help="Operands to operate on")    
    args = parser.parse_args()
    
    if args.operator.lower() == "help":
        print("Options:")
        for initial, name in operator_init_to_name.items():
            print(f"'{initial}': '{name}'")
        sys.exit()
  
    # Parse the string representations of operands into nested lists
    operands = [ast.literal_eval(arg) for arg in args.operands]

    get_operator(operator_init_to_name[args.operator])(operands)
    