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

class DisjointSet:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x, y = y, x 
        self.par[y] = x
        self.sz[x] += self.sz[y]
        self.cnt -= 1
        return True

    def size(self, x):
        return self.sz[self.find(x)]

    def components(self):
        return self.cnt


FN = "input/08.txt"
# FN = "sample.txt"
N = 1000

FILE = open(FN, "r")
points = [tuple(map(int, line.split(","))) for line in FILE.read().strip().split("\n")]

n = len(points)
dists = []
for i in range(n):
    for j in range(i+1, n):
        dists.append((dist(points[i], points[j]), i, j))
dists.sort()
uf = DisjointSet(n)

for _, i, j in dists[:N]:
    uf.union(i, j)

reps = set()
sizes = []
for u in range(n):
    rep = uf.find(u)
    if rep not in reps:
        reps.add(rep)
        sizes.append(uf.size(rep))
sizes.sort()
ans1 = prod(sizes[-3:])
print(ans1)

for _, i, j in dists[N:]:
    uf.union(i, j)
    if uf.components() == 1:
        ans2 = points[i][0] * points[j][0]
        break
print(ans2)