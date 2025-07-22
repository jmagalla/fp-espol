import numpy as np

pilots = np.loadtxt("pilots2024_lineal.txt",delimiter="|",dtype=str)

points = np.loadtxt("points2024_lineal.txt",delimiter="|",dtype=int)

print(points)

print(pilots)

#los pilotos con mas de 190 ptos
pilots[ points > 190 ]

#cuantos pilotos tienen mas de 190 ptos
print(points > 190)
mask = points > 190

print(mask.sum())
