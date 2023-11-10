import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def conclusion():
    print("--------------Task 1--------------")
    print(task1()[0])
    print("--------------Task 2--------------")
    print(task2(values, points)[0])
    print("--------------Task 3--------------")
    print(task3(values, points)[0])
    print("--------------Task 4--------------")
    print(task4())
    print("--------------Task 5--------------")
    print(task5()[0])
    print("--------------Task 6--------------")
    print(task6(points)[0])
    print("--------------Task 7--------------")
    print(task7(values, points))
    print("--------------Task 8--------------")
    print(task8_ggplot(values, points))
    print(task8_fivethirtyeight(values, points))
    print(task8_dark_background(values, points))

def task1():
    points = np.linspace(4, 6, 20)
    values = 2 / np.tan(points)
    return values, points

values, points = task1()

def task2(values, points):
    plt.plot(points, values, label='Функция (2 / tan(x))')
    plt.title('Простроение графика функции (2 / tan(x))', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend()
    plt.show()
    return "работает", plt

def task3(values, points):
    plt.scatter(points, values, marker='o', color=(0.5, 0.2, 0.8), label='Функция (2 / tan(x))')
    plt.title('Точечный график функции (2 / tan(x))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color=(0.8, 0.5, 0.2, 0.3), alpha=0.1)
    plt.show()
    return "работает", plt

def task4():
    uniform_samples = np.random.randint(low=0, high=100, size=1000)
    normal_samples = np.random.normal(loc=50, scale=10, size=1000).astype(int)
    plt.hist(uniform_samples, bins=20, color='blue', label='Равномерное распределение')
    plt.title('Гистограммы выборок')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.legend()
    plt.show()

    plt.hist(normal_samples, bins=30, color='red', alpha=0.5, label='Нормальное распределение')
    plt.title('Гистограммы выборок')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.legend()
    plt.show()
    return "работает"

def task5():
    sample = np.random.randint(1, 5, size=50)
    unique, counts = np.unique(sample, return_counts=True)
    frequency = dict(zip(unique, counts))
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    plt.pie(counts, labels=unique, colors=colors)
    plt.title('Круговая диаграмма')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    plt.legend(title='Числа', labels=label_percentages, loc='upper right')
    plt.show()
    plt.bar(unique, counts, color=colors)
    plt.title('Столбчатая диаграмма')
    plt.xlabel('Числа')
    plt.ylabel('Частота')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    for i in range(len(unique)):
        plt.annotate(label_percentages[i], (unique[i], counts[i]), ha='center', va='bottom')
    plt.show()
    return "работает", plt

def task6(points):
    X, Y = np.meshgrid(points, points)
    Z = (X - 1.5) ** 2 + (Y - 2) ** 2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Трехмерный график функции')
    plt.show()
    return "работает", plt

def task7(values, points):
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    axes[0, 0].set_facecolor('lightgray')
    axes[0, 1].set_facecolor('lightgray')
    axes[1, 0].set_facecolor('lightgray')
    axes[1, 1].set_facecolor('lightgray')

    axes[0, 0].plot(points, values)
    axes[0, 0].set_title('График функции', fontsize=12)
    axes[0, 0].set_xlabel('x', fontsize=10)
    axes[0, 0].set_ylabel('y', fontsize=10)

    axes[0, 1].scatter(points, values, marker='o', color=(0.5, 0.2, 0.8), label='Функция (2 / tan(x))')
    axes[0, 1].set_title('Точечный график функции (2 / tan(x))', fontsize=12)
    axes[0, 1].set_xlabel('x', fontsize=10)
    axes[0, 1].set_ylabel('y', fontsize=10)

    sample = np.random.randint(1, 5, size=50)
    unique, counts = np.unique(sample, return_counts=True)
    frequency = dict(zip(unique, counts))
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    axes[1, 0].pie(counts, labels=unique, colors=colors)
    axes[1, 0].set_title('Круговая диаграмма')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    axes[1, 0].legend(title='Числа', labels=label_percentages, loc='upper right')

    X, Y = np.meshgrid(points, points)
    Z = (X - 1.5) ** 2 + (Y - 2) ** 2
    axes[1, 1] = fig.add_subplot(224, projection='3d')
    axes[1, 1].plot_surface(X, Y, Z)
    axes[1, 1].set_title('Трехмерный график функции', fontsize=12)
    axes[1, 1].set_xlabel('X', fontsize=10)
    axes[1, 1].set_ylabel('Y', fontsize=10)
    axes[1, 1].set_zlabel('Z', fontsize=10)
    plt.suptitle('Сетка 2x2 из 4 графиков', fontsize=16)
    plt.tight_layout()
    plt.show()
    return "работает"

def task8_ggplot(values, points):
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    sample = np.random.randint(1, 5, size=50)
    unique, counts = np.unique(sample, return_counts=True)
    frequency = dict(zip(unique, counts))
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    X, Y = np.meshgrid(points, points)
    Z = (X - 1.5) ** 2 + (Y - 2) ** 2
    plt.suptitle('Сетка 2x2 из 4 графиков (ggplot)', fontsize=16)
    plt.tight_layout()
    #---------------------------------------------
    plt.style.use('ggplot')
    axes[0, 0].plot(points, values)
    axes[0, 0].set_title('График функции', fontsize=12)
    axes[0, 0].set_xlabel('x', fontsize=10)
    axes[0, 0].set_ylabel('y', fontsize=10)

    axes[0, 1].scatter(points, values, marker='o', color=(0.5, 0.2, 0.8), label='Функция (2 / tan(x))')
    axes[0, 1].set_title('Точечный график функции (2 / tan(x))', fontsize=12)
    axes[0, 1].set_xlabel('x', fontsize=10)
    axes[0, 1].set_ylabel('y', fontsize=10)

    axes[1, 0].pie(counts, labels=unique, colors=colors)
    axes[1, 0].set_title('Круговая диаграмма')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    axes[1, 0].legend(title='Числа', labels=label_percentages, loc='upper right')

    axes[1, 1] = fig.add_subplot(224, projection='3d')
    axes[1, 1].plot_surface(X, Y, Z)
    axes[1, 1].set_title('Трехмерный график функции', fontsize=12)
    axes[1, 1].set_xlabel('X', fontsize=10)
    axes[1, 1].set_ylabel('Y', fontsize=10)
    axes[1, 1].set_zlabel('Z', fontsize=10)
    plt.grid(True)
    plt.show()
    return "работает"

def task8_fivethirtyeight(values, points):
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    sample = np.random.randint(1, 5, size=50)
    unique, counts = np.unique(sample, return_counts=True)
    frequency = dict(zip(unique, counts))
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    X, Y = np.meshgrid(points, points)
    Z = (X - 1.5) ** 2 + (Y - 2) ** 2
    plt.suptitle('Сетка 2x2 из 4 графиков (fivethirtyeight)', fontsize=16)
    plt.tight_layout()
    #-------------------------------------------------
    plt.style.use('fivethirtyeight')
    axes[0, 0].plot(points, values)
    axes[0, 0].set_title('График функции', fontsize=12)
    axes[0, 0].set_xlabel('x', fontsize=10)
    axes[0, 0].set_ylabel('y', fontsize=10)

    axes[0, 1].scatter(points, values, marker='o', color=(0.5, 0.2, 0.8), label='Функция (2 / tan(x))')
    axes[0, 1].set_title('Точечный график функции (2 / tan(x))', fontsize=12)
    axes[0, 1].set_xlabel('x', fontsize=10)
    axes[0, 1].set_ylabel('y', fontsize=10)

    axes[1, 0].pie(counts, labels=unique, colors=colors)
    axes[1, 0].set_title('Круговая диаграмма')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    axes[1, 0].legend(title='Числа', labels=label_percentages, loc='upper right')

    axes[1, 1] = fig.add_subplot(224, projection='3d')
    axes[1, 1].plot_surface(X, Y, Z)
    axes[1, 1].set_title('Трехмерный график функции', fontsize=12)
    axes[1, 1].set_xlabel('X', fontsize=10)
    axes[1, 1].set_ylabel('Y', fontsize=10)
    axes[1, 1].set_zlabel('Z', fontsize=10)
    plt.grid(True)
    plt.show()
    return "работает"

def task8_dark_background(values, points):
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    sample = np.random.randint(1, 5, size=50)
    unique, counts = np.unique(sample, return_counts=True)
    frequency = dict(zip(unique, counts))
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    X, Y = np.meshgrid(points, points)
    Z = (X - 1.5) ** 2 + (Y - 2) ** 2
    plt.suptitle('Сетка 2x2 из 4 графиков (dark_background)', fontsize=16)
    plt.tight_layout()
    #---------------------------------------------------------------------
    plt.style.use('dark_background')
    axes[0, 0].plot(points, values)
    axes[0, 0].set_title('График функции', fontsize=12)
    axes[0, 0].set_xlabel('x', fontsize=10)
    axes[0, 0].set_ylabel('y', fontsize=10)

    axes[0, 1].scatter(points, values, marker='o', color=(0.5, 0.2, 0.8), label='Функция (2 / tan(x))')
    axes[0, 1].set_title('Точечный график функции (2 / tan(x))', fontsize=12)
    axes[0, 1].set_xlabel('x', fontsize=10)
    axes[0, 1].set_ylabel('y', fontsize=10)

    axes[1, 0].pie(counts, labels=unique, colors=colors)
    axes[1, 0].set_title('Круговая диаграмма')
    label_percentages = ['%.2f%%' % (count * 100 / len(sample)) for count in counts]
    axes[1, 0].legend(title='Числа', labels=label_percentages, loc='upper right')

    axes[1, 1] = fig.add_subplot(224, projection='3d')
    axes[1, 1].plot_surface(X, Y, Z)
    axes[1, 1].set_title('Трехмерный график функции', fontsize=12)
    axes[1, 1].set_xlabel('X', fontsize=10)
    axes[1, 1].set_ylabel('Y', fontsize=10)
    axes[1, 1].set_zlabel('Z', fontsize=10)
    plt.grid(True)
    plt.show()
    return "работает"

conclusion()
