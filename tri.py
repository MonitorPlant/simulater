import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig = plt.figure(figsize=(5, 5))

ax = fig.add_subplot(111)

p = pat.Polygon(xy = [(.2, 0.2), (0.8, 0.2), (0.5, 0.8)], fc = "lightblue", ec = "darkred")

ax.add_patch(p)

plt.show()


