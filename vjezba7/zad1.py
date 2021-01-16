import numpy as np

point1 = np.array((1, 2, 3))
point2 = np.array((3, 2, 1))

udaljenost = np.linalg.norm(point1 - point2)

print(udaljenost)
