import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def draw_boxes(data):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    colors = [
        (0.7, 0.8, 1.0), (1.0, 0.7, 0.7), (0.7, 1.0, 0.7),
        (1.0, 1.0, 0.7), (1.0, 0.7, 1.0), (0.7, 1.0, 1.0)
    ]
    for i, (idx, x, y, z, dx, dy, dz) in enumerate(data):
        xx = [x, x+dx, x+dx, x, x, x+dx, x+dx, x]
        yy = [y, y, y+dy, y+dy, y, y, y+dy, y+dy]
        zz = [z, z, z, z, z+dz, z+dz, z+dz, z+dz]
        verts = [
            [(xx[0], yy[0], zz[0]), (xx[1], yy[1], zz[1]), (xx[2], yy[2], zz[2]), (xx[3], yy[3], zz[3])],
            [(xx[4], yy[4], zz[4]), (xx[5], yy[5], zz[5]), (xx[6], yy[6], zz[6]), (xx[7], yy[7], zz[7])],
            [(xx[0], yy[0], zz[0]), (xx[1], yy[1], zz[1]), (xx[5], yy[5], zz[5]), (xx[4], yy[4], zz[4])],
            [(xx[2], yy[2], zz[2]), (xx[3], yy[3], zz[3]), (xx[7], yy[7], zz[7]), (xx[6], yy[6], zz[6])],
            [(xx[1], yy[1], zz[1]), (xx[2], yy[2], zz[2]), (xx[6], yy[6], zz[6]), (xx[5], yy[5], zz[5])],
            [(xx[4], yy[4], zz[4]), (xx[7], yy[7], zz[7]), (xx[3], yy[3], zz[3]), (xx[0], yy[0], zz[0])]
        ]
        color = colors[i % len(colors)]
        ax.add_collection3d(Poly3DCollection(verts, facecolors=[color], linewidths=1.5, edgecolors='k', alpha=0.5))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()
