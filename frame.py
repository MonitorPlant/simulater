import itertools
import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as pat
from matplotlib import animation

fig = plt.figure(figsize=(8, 8))

def main():
    ax = fig.add_subplot(111)
    x_1 = np.linspace(-3000, 3000, 6000)
    y_1 = x_1 - x_1
    y_2 = np.linspace(0, 6000, 6000)
    x_2 = y_2 - y_2

    #枠を描画
    #下枠
    frame_bottom_x = np.linspace(-3000, 3000, 2)
    frame_bottom_y = frame_bottom_x - frame_bottom_x - 3000
    ax.plot(frame_bottom_x, frame_bottom_y)

    #上枠
    frame_ceiling_x = np.linspace(-3000, 3000, 2)
    frame_ceiling_y = frame_ceiling_x - frame_bottom_x + 3000
    ax.plot(frame_ceiling_x, frame_ceiling_y)

    #左枠
    frame_left_y = np.linspace(-3000, 3000, 2)
    frame_left_x = frame_left_y - frame_left_y - 3000
    ax.plot(frame_left_x, frame_left_y)

    #右枠
    frame_right_y = np.linspace(-3000, 3000, 2)
    frame_right_x = frame_right_y - frame_right_y + 3000
    ax.plot(frame_right_x, frame_right_y)

    
   # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()

