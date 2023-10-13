import numpy as np

def print_mat(mat):
    mat_shape = mat.shape
    b = ""
    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            #print(round(mat[i, j], 3), end=" ")
            b += str(mat[i, j]) + '\t'
        print(b)
        b = ""

def print_mat_exp(mat):
    mat_shape = mat.shape
    b = ""
    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            # print(round(mat[i, j], 3), end=" ")
            b += (str(int(mat[i, j]/10000000))+"+"+"10^10000000 ") + 3*'\t'
        print(b)
        b = ""

def print_mat_round(mat):
    mat_shape = mat.shape
    b = ""
    for i in range(mat_shape[0]):
        for j in range(mat_shape[1]):
            # print(round(mat[i, j], 3), end=" ")
            b += str(round(mat[i, j], 3)) + '\t'
        print(b)
        b = ""

def conclusion():
    print("--------------Task 1--------------")
    print(task1())
    print()
    print("--------------Task 2--------------")
    print_mat(task2(my_array))
    print("--------------Task 3--------------")
    print_mat(task3(A))
    print("--------------Task 4--------------")
    print_mat(task4())
    print("--------------Task 5--------------")
    print(task5(A1, B))
    print("--------------Task 6--------------")
    print_mat(task6(A1, B))
    print("--------------Task 7--------------")
    print_mat(task7(A1, B)[1])
    print("--------------Task 8--------------")
    print(task8(A2, B1))
    print("--------------Task 9--------------")
    print_mat_exp(task9(A2, B1))
    print("--------------Task 10--------------")
    print(task10())

def task1():
    return np.arange(10, 70, 2)

my_array = task1()

def task2(my_array):
    return np.reshape(my_array, (6, 5)).T

A = task2(my_array)

def task3(A):
    A1 = A * 2.5
    A1[0, :] -= 5
    return A1

A1 = task3(A)

def task4():
    return np.random.randint(0, 11, (6, 3))

B = task4()

def task5(A1, B):
    a = [0] * len(A1)
    for i in range(len(A1)):
        for j in range(len(A1[0])):
            a[i] = A1[i, j] + a[i]
    b = [0] * len(B[0])
    for i in range(len(B[0])):
        for j in range(len(B)):
            b[i] = B[j, i] + b[i]
    return len(a), len(b)

def task6(A1, B):
    return np.dot(A1, B)

def task7(A1, B):
    A1 = np.delete(A1, 2, 1)
    for i in range(3):
        a = np.random.randint(10, 20, (6, 1))
        B = np.c_[B, a]
    print_mat(A1)
    print()
    return A1, B

A2, B1 = task7(A1, B)

def task8(A2, B1):
    a_det = np.linalg.det(A2)
    b_det = np.linalg.det(B1)
    if a_det != 0:
        a_inv = np.linalg.inv(A2)
        print(a_inv)
    else: print("a_inv does not exist")
    if b_det != 0:
        b_inv = np.linalg.inv(B1)
        print_mat_round(b_inv)
    else: print("b_inv does not exist")
    return a_det, b_det

def task9(A2, B1):
    A2 = np.linalg.matrix_power(A2, 6)
    B1 = np.linalg.matrix_power(B1, 14)
    print_mat_exp(A2)
    print()
    return B1

def task10():
    a = np.array([[2.7, 4, -3, 3], [2, -16, -9, 0], [8, -5, -3, -4], [2, 0, -1.7, -1.7]])
    b = np.array([2, 8, 0, -4])
    x = np.linalg.solve(a, b)
    return x

conclusion()

array_test = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]
mat_test = np.reshape(array_test, (2, 5))
print_mat(mat_test)
