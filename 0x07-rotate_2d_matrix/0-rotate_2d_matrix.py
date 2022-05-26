#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    j = len(matrix)
    rev_mat = matrix[:]
    matrix.clear()
    i = 0
    while i < len(rev_mat[0]):
        arr = []
        k = j - 1
        while k >= 0:
            arr.append(rev_mat[k][i])
            k -= 1
        matrix.append(arr)
        i += 1
