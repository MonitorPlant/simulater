import itertools
import math

import numpy as np

import matplotlib
from matplotlib import pyplot as plt
from matplotlib import patches as pat
from matplotlib import animation

import move

#matplotlib.use('TKAgg')
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

def _update(frame, x, y):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # サブプロットを用意


    # フィールドの枠線を描画(6000x6000mm)
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


    move.update_coord(frame)
    #三角形の座標を更新
    #px = 1 * math.sin(frame)
    #py = 1 * math.cos(frame)
    px = move.get_x()
    py = move.get_y()

    p = pat.Polygon(xy = [(px, py), (px + 200, py), (px + 100, py + 200)], fc = "lightblue", ec = "darkred")
    ax.add_patch(p)
    # データを更新 (追加) する
    # x.append(frame)
    x.append(0)
    # y.append(math.sin(frame))
    y.append(0)

    # ロボットを表現する三角形を描画
    #p = pat.Polygon(xy = [
    #    (move.get_x(), move.get_y()),
    #    (move.get_x() + 6, move.get_y()),
    #    (move.get_x() - 6, move.get_y() + 6)
    #    ],
    #    fc = "lightblue", ec = "darkred")

    #ax.add_patch(p)

    # フィールドの枠線を描画
    

    # 折れ線グラフを再描画する
    plt.plot(x, y)


def main():
    # 描画領域
    # 描画するデータ
    x = []
    y = []

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x, y),  # 関数の引数 (フレーム番号を除く)
        'interval': 10,  # 更新間隔 (ミリ秒)
        'frames': itertools.count(0, 0.01),  # フレーム番号を無限に生成するイテレータ
    }

    anime = animation.FuncAnimation(**params)

    # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()

