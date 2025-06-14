import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

data = [
    (0, 0, 11, 0, 8, 5, 3),
    (1, 3, 0, 24, 12, 15, 12),
    (2, 15, 18, 24, 15, 12, 12),
    (3, 15, 3, 24, 12, 15, 12),
    (4, 0, 15, 22, 15, 12, 12),
    (5, 18, 0, 12, 12, 15, 12),
    (6, 3, 3, 12, 15, 12, 12),
    (7, 15, 18, 12, 15, 12, 12),
    (8, 0, 15, 10, 12, 15, 12),
    (9, 8, 0, 0, 12, 15, 12),
    (10, 0, 16, 5, 11, 8, 5),
    (11, 0, 0, 5, 8, 11, 5),
    (12, 13, 15, 4, 8, 11, 5),
    (13, 0, 16, 0, 11, 8, 5),
    (14, 0, 0, 0, 8, 11, 5),
    (15, 22, 0, 0, 8, 5, 11),
    (16, 1, 25, 0, 11, 5, 8),
    (17, 21, 6, 8, 9, 12, 4),
    (18, 21, 18, 8, 9, 12, 4),
    (19, 21, 18, 4, 9, 12, 4),
    (20, 21, 6, 4, 9, 12, 4),
    (21, 12, 15, 0, 9, 12, 4),
    (22, 21, 18, 0, 9, 12, 4),
    (23, 21, 5, 0, 9, 12, 4)
]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i, (idx, x, y, z, dx, dy, dz) in enumerate(data):
    # Các đỉnh của box
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

    color = np.random.rand(3,)
    ax.add_collection3d(Poly3DCollection(verts, facecolors=[color], linewidths=1, edgecolors='k', alpha=0.4))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()