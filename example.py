from math import sin, pi, cos
import time
import matplotlib.pyplot as plt
from map.BinarySearchMatrix import BinarySearchMatrix
import random


def distance(point):
    def function(e):
        square_distance = 0
        for p_index in range(0, len(point)):
            square_distance = square_distance + (point[p_index] - e[p_index]) ** 2
        return square_distance

    return function


if __name__ == '__main__':
    x = []
    y = []
    points = []
    b_map = BinarySearchMatrix(2)
    for i in range(0, 1000):
        n = random.randint(0, 100)
        p = [n]
        x.append(n)
        n = random.randint(0, 100)
        p.append(n)
        y.append(n)
        points.append([x[-1], y[-1]])
        b_map.add(p, str(p[0]) + "," + str(p[1]))
    plt.plot(x, y, "ro")

    x = []
    y = []
    for i in range(0, 360):
        rad = pi * i / 180
        y.append(sin(rad) * 20 + 25)
        x.append(cos(rad) * 20 + 25)
    plt.plot(x, y)

    t0 = time.time()
    l = b_map.radial_knn([25, 25], 20)
    print("Time: " + str(time.time() - t0))
    print(l)

    t0 = time.time()
    points.sort(key=distance([25, 25]))
    print("Time: " + str(time.time() - t0))
    print(points[0:len(l)])

    plt.ylabel('Data')
    plt.show()
