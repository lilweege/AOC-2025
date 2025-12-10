from collections import Counter, defaultdict, deque
from itertools import pairwise, product
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf, dist, prod
from operator import ior, iand, xor
import re
# import sys
# sys.setrecursionlimit(9999)

FN = "input/09.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
points = [tuple(map(int, line.split(","))) for line in FILE.read().strip().split("\n")]

n = len(points)
ans1 = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        ans1 = max(ans1, (abs(y1-y2)+1) * (abs(x1-x2)+1))
print(ans1)

cX = {}
cY = {}
for x, _ in sorted(points, key=lambda t: t[0]):
    if x not in cX:
        cX[x] = len(cX)
for _, y in sorted(points, key=lambda t: t[1]):
    if y not in cY:
        cY[y] = len(cY)

def compress(x, y):
    return cX[x], cY[y]

g = [[' ' for _ in range(len(cX))] for _ in range(len(cY))]
points.append(points[0])
for (x1, y1), (x2, y2) in pairwise(points):
    cx1, cy1 = compress(x1, y1)
    cx2, cy2 = compress(x2, y2)
    if cx2 < cx1:
        cx1, cx2 = cx2, cx1
    if cy2 < cy1:
        cy1, cy2 = cy2, cy1
    if cx1 == cx2:
        for i in range(cy1, cy2+1):
            g[i][cx1] = '#'
    else:
        for j in range(cx1, cx2+1):
            g[cy1][j] = '#'

# s = 1, 2
s = compress(*points[0])
s = s[1]-1, s[0]+1

q = deque([s])
while q:
    i, j = q.popleft()
    if g[i][j] == '#':
        continue
    g[i][j] = '#'
    for ni, nj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
        if 0 <= ni < len(g) and 0 <= nj < len(g[0]):
            q.append((ni, nj))
# for i in range(len(g)):
#     for j in range(len(g[0])):
#         c = g[i][j]
#         if (i, j) == s:
#             c = 'S'
#         print(c, end="")
#     print()


ans2 = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        cx1, cy1 = compress(x1, y1)
        x2, y2 = points[j]
        cx2, cy2 = compress(x2, y2)
        if cx2 < cx1:
            cx1, cx2 = cx2, cx1
        if cy2 < cy1:
            cy1, cy2 = cy2, cy1
        if all(g[y][x] == '#' for x in range(cx1, cx2+1) for y in range(cy1, cy2+1)):
            ans2 = max(ans2, (abs(y1-y2)+1) * (abs(x1-x2)+1))
print(ans2)
