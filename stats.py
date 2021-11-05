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

x = [np.log(float(item.replace(",",".").strip("\n"))) for item in get_column(array2D, 1)]
y = [np.log(float(item.replace(",",".").strip("\n"))) for item in get_column(array2D, 0)]

func = np.polyfit(x, y, 1)

poly = np.poly1d(func)

print(poly)

fromFunc = [poly(item) for item in x]

resids = [y[i] - fromFunc[i] for i in range(len(y))]

plt.grid(color='gray', linestyle='-', linewidth=1)

def scatter():
    plt.scatter(x,y)
    plt.ylabel("log(Weight (lbs))", fontsize=12)
    plt.xlabel("log(Length (in))", fontsize=12)
    plt.show()

def scatterfit():
    plt.scatter(x,y)
    plt.plot(x, fromFunc, 'r', label = 'log(ŷ) = -4.418 + 3.286log(x)')
    plt.legend(loc='upper left')
    plt.ylabel("log(Weight (lbs))", fontsize=12)
    plt.xlabel("log(Length (in))", fontsize=12)
    plt.title("Power: r = 0.9720805" + " r² = 0.9449404",fontsize=15)
    plt.show()

def resid():
    plt.scatter(x,resids)
    plt.title("Residual Plot")
    plt.ylabel("log(Residuals (lbs))", fontsize=12)
    plt.xlabel("log(Length (in))", fontsize=12)
    plt.show()

resid()