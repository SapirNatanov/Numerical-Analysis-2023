'''
Date: 19/2/2024
Group: Sapir Natanov 322378068
Dor Maudi 207055138
Noa Yasharzadeh 208595157
Segev Isaac 207938085
Git:https://github.com/SapirNatanov/Numerical-Analysis-2023.git
Name: Sapir Natanov 322378068
'''

import numpy as np
from Matrix.inverse_matrix import inverse
from colors import bcolors
from matrix_utility import print_matrix

def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    A_inv = inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    # print(bcolors.OKBLUE, "A:", bcolors.ENDC)
    # print_matrix(A)

    # print(bcolors.OKBLUE, "inverse of A:", bcolors.ENDC)
    # print_matrix(A_inv)

    print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")

    #print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)

    return cond


if __name__ == '__main__':

    A = np.array([[-1, -2, 5],
                  [4, -1, 1],
                  [1, 6, 2]])
    print(f"input:\n{A}")
    cond = condition_number(A)

    #print(bcolors.OKGREEN, "\n condition number: ", cond, bcolors.ENDC)






