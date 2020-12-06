# !/home/dletran/miniconda3/bin/python
# Odds Ratio calculator
# Author: Duke LeTran
# Date: 2020-12-05

import numpy as np
import sys

def calculate(ls_flat):
    numerator = ls_flat[0] * ls_flat[3]
    denominator = ls_flat[1] * ls_flat[2]
    answer = round(numerator / denominator, 4)
    return str(answer)

def value_error():
    error_msg = 'Must be a number. '
    if sys.platform == 'win32':
        error_msg += 'Press ctl+Z to exit (on windows).'
    else:
        error_msg += 'Press ctl+D to exit (on linux or mac).'
    print(error_msg)


def main():
    ls = ['a', 'b','c','d']
    arr = np.array([ls[:2], ls[2:]])
    print("Odds-Ratio Calculator 1.0 by Duke LeTran (2020-12-05)")
    print("Enter 4 space-separated-numbers. See below:")
    print(arr)
    while(1):
        #### I. READ: try to read input
        try:
            ls_flat = [float(input(f'Enter {x} >> ')) for x in ls]
        except EOFError:
            sys.exit()
        except:
            value_error()
            continue

        #### II. CALCULATE: try to calculate
        try:
            answer = calculate(ls_flat)
        except IndexError as e:
            print("There must be exactly two elements per row.", e)
            continue

        #### III. PRINT: print answer
        print(np.array([ls_flat[:2], ls_flat[2:]]))
        print(f"^Matrix. The calculated odds-ratio is... {answer}")
        try:
            result = input('Continue? (y/n) >> ')
            if result.lower() in ['n', 'no']:
                sys.exit()
        except EOFError:
            sys.exit()


if __name__ == '__main__':
    main()