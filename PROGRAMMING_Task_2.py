import numpy as np
import math
import scipy as sp
import sympy as sym

x = sym.Symbol('x')

def conclusion():
    print("--------------Task 1--------------")
    print(task1())
    print("--------------Task 2--------------")
    print(task2())
    print("--------------Task 3--------------")
    print(task3()[0])
    print("--------------Task 4--------------")
    print(task4())
    print("--------------Task 5--------------")
    print(task5())

def f(x):
    return (2 / math.tan(x))

def task1():
    return sp.misc.derivative(f, 1, n=1, dx=0.1), sp.misc.derivative(f, 1, n=2, dx=0.1)

def task2():
    return sym.diff(2/sym.tan(x))

def task3():
    return sp.integrate.quad(f, 4, 6)

def task4():
    return sym.integrate(2/sym.tan(x))

def func(x):
    return (x[0]-1.5)**2 + (x[1]-2)**2 + (x[2]-2.5)**2

def constraint1(x):
    return 2*x[0] + 2*x[1] - 6

def constraint2(x):
    return 2*x[0] + 2*x[2] - 17

def task5():
    x0 = [0, 0, 0]
    constraints = [{'type': 'eq', 'fun': constraint1}, {'type': 'eq', 'fun': constraint2}]
    bounds = [(0, None), (0, None), (0, None)]  # Все переменные неотрицательны
    result = sp.optimize.minimize(func, x0, bounds=bounds, constraints=constraints)
    return result

conclusion()
