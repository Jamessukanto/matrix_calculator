import sys
import argparse
import ast

from operators import initial_to_operation


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="arg parser")
    parser.add_argument("operator", type=str, help="Operator to perform")
    parser.add_argument("operands", type=str, nargs="*", help="Operands to operate on")    
    args = parser.parse_args()
    
    if args.operator.lower() == "help":
        print("Options:")
        for initial, operation in initial_to_operation.items():
            print(f"'{initial}': '{operation.__name__}'")
        sys.exit()
  
    # parse string representations of operands into nested lists
    operands = [ast.literal_eval(arg) for arg in args.operands]

    # perform operations
    initial_to_operation[args.operator](operands)