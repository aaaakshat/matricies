#!/usr/bin/env python3

# Time Bound Computation: NunPy vs Handmade algorithms.

import numpy as np
from time import time
from random import random
from matplotlib import pyplot as plt


def gen_rand_matrix(rows, cols):
    a = np.random.rand(rows, cols).tolist()
    a = [[int(i*10) for i in j] for j in a]
    return a


def matrix_mult(matrix1, matrix2):
    row1 = len(matrix1)
    row2 = len(matrix2)
    col1 = len(matrix1[0])
    col2 = len(matrix2[0])

    if col1 != row2:
        print("Incompatible matricies. #col1 must equal #row2")
        print(col1, row2)
        return None

    output = [[None for i in range(row1)] for i in range(col2)]
    transposed = transpose(matrix2)
    for i in range(row1):
        for j in range(col2):
            row = matrix1[i]
            col = transposed[j]
            prod = [a*b for a, b in zip(row, col)]
            output[i][j] = sum(prod)
    return output


def numpy_matrix_mult(matrix1, matrix2):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    output = np.matmul(matrix1,matrix2)
    return output.tolist()

def run():
    print("Multiply 2 nxn matricies. Enter size n")
    n = int(input())
    m1 = gen_rand_matrix(n, n)
    m2 = gen_rand_matrix(n, n)

    print("MULTIPLY BY OWN ALGORITHM")
    start = time()
    matrix_mult(m1,m2)
    stop = time()
    print(str(stop-start) + " seconds taken")

    print("MULTIPLY WITH NUMPY")
    start = time()
    numpy_matrix_mult(m1, m2)
    stop = time()
    print(str(stop-start) + " seconds taken")

def run_plot():
    print("What nxn size to test until?")
    n = int(input())
    my_time = []
    np_time = []
    ns = []

    for i in range(2,n):
        ns.append(i)
        m1 = gen_rand_matrix(n, n)
        m2 = gen_rand_matrix(n, n)

        start = time()
        matrix_mult(m1, m2)
        stop = time()
        my_time.append(stop-start)

        start = time()
        numpy_matrix_mult(m1, m2)
        stop = time()
        np_time.append(stop-start)
    
    plt.plot(ns, my_time, label='my_time')
    plt.plot(ns, np_time, label='np_time')
    plt.legend(loc='upper center', ncol = 2)
    plt.show()

def transpose(matrix):
    output = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            output[j][i] = matrix[i][j]
    return output

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


run_plot()
