import numpy as np
import scipy as sp

def print_matr(mat):
    for row in mat:
        for value in row:
            print(f"{value:6.1f}", end=" ")
        print()

def conclusion():
    print("--------------Task 1--------------")
    print_matr(task1())
    print("--------------Task 2--------------")
    task2(my_array)
    print("--------------Task 3--------------")
    task3(my_array, P, L, U)
    print("--------------Task 4--------------")
    print(task4()[0])
    print("")
    print(task4()[1])
    print("--------------Task 5--------------")
    task5(uniform_sample, normal_sample)
    print("--------------Task 6--------------")
    print(task6(uniform_sample))

def task1():
    return np.array([[2.7, 4, -3, 3], [2, -16, -9, 0], [8, -5, -3, -4], [2, 0, -1.7, -1.7]])

my_array = task1()

def task2(A):
    P, L, U = sp.linalg.lu(A)
    print_matr(P)
    print("")
    print_matr(L)
    print("")
    print_matr(U)
    return P, L, U

P, L, U = task2(my_array)

def task3(matrix, P, L, U):
    det_matrix = np.linalg.det(matrix)
    print(det_matrix)
    print("")
    det_P_inv = np.linalg.det(np.linalg.inv(P))
    print(det_P_inv)
    print("")
    prod_diag_LU = np.prod(np.diag(L)) * np.prod(np.diag(U))
    print(prod_diag_LU)

#A1 = task3(A)

def task4():
    uniform_sample = np.random.randint(low=0, high=100, size=100)
    normal_sample = np.random.normal(loc=50, scale=10, size=100).astype(int)
    return uniform_sample, normal_sample

uniform_sample, normal_sample = task4()

def task5(uniform_sample, normal_sample):
    uniform_mean = np.mean(uniform_sample)
    print(uniform_mean)
    print("")
    uniform_mode = sp.stats.mode(uniform_sample)
    print(uniform_mode)
    print("")
    uniform_median = np.median(uniform_sample)
    print(uniform_median)
    print("")
    uniform_min = np.min(uniform_sample)
    print(uniform_min)
    print("")
    uniform_max = np.max(uniform_sample)
    print(uniform_max)
    print("")
    uniform_std = np.std(uniform_sample)
    print(uniform_std)
    print("-----------------------")

    normal_mean = np.mean(normal_sample)
    print(normal_mean)
    print("")
    normal_mode = sp.stats.mode(normal_sample)
    print(normal_mode)
    print("")
    normal_median = np.median(normal_sample)
    print(normal_median)
    print("")
    normal_min = np.min(normal_sample)
    print(normal_min)
    print("")
    normal_max = np.max(normal_sample)
    print(normal_max)
    print("")
    normal_std = np.std(normal_sample)
    print(normal_std)

def task6(uniform_sample):
    p_value = sp.stats.chisquare(uniform_sample).pvalue
    return p_value

conclusion()
