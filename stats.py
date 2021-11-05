#VA
import matplotlib.pyplot as plt
import numpy as np

def get_column(array2D, column):

    column_list = []

    for row in array2D:
        column_list.append(row[column])

    return column_list

array2D = []

with open("gat.txt", 'r') as f:
    for line in f.readlines():
        array2D.append(line.split('\t'))

x = [(float(item.replace(",",".").strip("\n"))) for item in get_column(array2D, 1)]
y = [(float(item.replace(",",".").strip("\n"))) for item in get_column(array2D, 0)]

func = np.polyfit(x, y, 1)

poly = np.poly1d(func)

fromFunc = [poly(item) for item in x]

resids = [y[i] - fromFunc[i] for i in range(len(y))]

plt.grid(color='gray', linestyle='-', linewidth=1)

def scatter():
    plt.scatter(x,y)
    plt.ylabel("Weight (lbs)", fontsize=12)
    plt.xlabel("Length (in)", fontsize=12)
    plt.show()

def scatterfit():
    plt.scatter(x,y)
    plt.plot(x, fromFunc, 'r', label = 'y = -393.264 + 5.902')
    plt.legend(loc='upper left')
    plt.ylabel("Weight (lbs)", fontsize=12)
    plt.xlabel("Length (in)", fontsize=12)
    plt.title("Linear: r = 0.9144007" + " r² = 0.8361287",fontsize=15)
    plt.show()

scatter()