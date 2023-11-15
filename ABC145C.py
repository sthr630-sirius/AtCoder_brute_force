import itertools
import math
import numpy as np

n = int(input())
position = []
distance = []

for _ in range(n):
    x, y = map(float, input().split())
    position.append([x, y])

for p in itertools.permutations(position):
    #print(p)
    dist = 0
    for i in range(len(p)-1):
        x1 = p[i][0]
        y1 = p[i][1]
        x2 = p[i+1][0]
        y2 = p[i+1][1]
        dist += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    distance.append(dist)

    #print("------------")

#print(distance)
print(np.average(distance))