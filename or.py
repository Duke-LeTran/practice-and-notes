# !/home/dletran/miniconda3/bin/python
# Odds Ratio calculator
# Author: Duke LeTran
# Date: 2020-12-05

import numpy as np

def calculate(row_a, row_b):
    numerator = row_a[0] * row_b[1]
    denominator = row_a[1] * row_b[0]
    answer = round(numerator / denominator, 4)
    return answer

def main():
    print("Odds-Ratio Calculator 1.0 (2020-11-05), by Duke LeTran")
    print("The numbers must be entered L-to-R, separated by a single space.")

    ls_row_a = [float(x.strip()) for x in input('Enter the first row >> ').split(' ')]
    ls_row_b = [float(x.strip()) for x in input('Enter the second row >> ').split(' ')]

    answer = str(calculate(ls_row_a, ls_row_b))
    print(np.array([ls_row_a, ls_row_b]))
    print(f"^Matrix. The calculated odds-ratio is... {answer}")
    #print()
    #print()

if __name__ == '__main__':
    main()