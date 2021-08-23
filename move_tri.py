import itertools
import math

import numpy as np

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as pat
from matplotlib import animation

matplotlib.use('TKAgg')
fig = plt.figure(figsize=(5, 5))

#ax = fig.add_subplot(111)

#p = pat.Polygon(xy = [(.2, 0.2), (0.8, 0.2), (0.5, 0.8)], fc = "lightblue", ec = "darkred")

#ax.add_patch(p)

#plt.show()

def _update(frame, x, y):
    plt.cla()

    ax = fig.add_subplot(111)

    px = 1 * math.sin(frame)
    py = 1 * math.cos(frame)

    p = pat.Polygon(xy = [(px, py), (px + 0.6, py), (px + 0.3, py + 0.6)], fc = "lightblue", ec = "darkred")
    ax.add_patch(p)

    x.append(0)
    y.append(0)

    plt.show()

def main():
    x = []
    y = []

    params = {
            'fig': fig,
            'func': _update,
            'fargs': (x, y),
            'interval': 10, # 10ms
            'frames': itertools.count(0, 0.1),
    }

    anime = animation.FuncAnimation(**params)

    plt.show()

if __name__ == '__main__':
    main()

