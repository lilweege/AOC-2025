from collections import Counter, defaultdict, deque
from itertools import pairwise, product
from copy import deepcopy
from functools import cache, partial, reduce
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf
from operator import ior, iand, xor
import re
# import sys
# sys.setrecursionlimit(9999)

FN = "input/04.txt"
# FN = "sample.txt"

FILE = open(FN, "r")

s = FILE.read().strip()
grid = [list(r) for r in s.split("\n")]
n, m = len(grid), len(grid[0])
def iterate():
    global grid
    ans = 0
    nxt = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                cnt = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == dj == 0: continue
                        if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == '@':
                            cnt += 1
                if cnt < 4:
                    ans += 1
                    nxt[i][j] = '.'
    grid = nxt
    return ans

ans = iterate()
print(ans)
while (add := iterate()):
    ans += add
print(ans)