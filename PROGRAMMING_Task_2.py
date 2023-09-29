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
    return sp.misc.derivative(f, 1, n=1, dx=1e-6), sp.misc.derivative(f, 1, n=2, dx=1e-6)

def task2():
    return sym.diff(2/sym.tan(x))

def task3():
    return sp.integrate.quad(f, 4, 6)

def task4():
    return sym.integrate(2/sym.tan(x))

def task5():


conclusion()
