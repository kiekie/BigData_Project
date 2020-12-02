import sys
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
x = []
y = []
z = []

for line in sys.stdin:
    words = line.split(',')
    x.append(int(words[0]))
    y.append(int(words[1]))
    z.append(int(words[2]))

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
ax.set_zlabel('Z', fontdict={'size': 1700000, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 6200, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 90, 'color': 'red'})
ax.set_title('Hot line')

plt.savefig('c1' + '_labeled.png')