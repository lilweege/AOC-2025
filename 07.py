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

FN = "input/07.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
g = [list(r) for r in FILE.read().strip().split("\n")]
g = g[::2]
n, m = len(g), len(g[0])
s = g[0].index('S')

g[0][s] = '|'
ans1 = 0
for prow, row in pairwise(g):
    for j in range(m):
        if prow[j] == '|':
            if row[j] == '^':
                ans1 += 1
                row[j-1] = '|'
                row[j+1] = '|'
            elif row[j] == '.':
                row[j] = '|'
print(ans1)

dp = [[0] * m for _ in range(n)]
dp[0][s] = 1
for i in range(1, n):
    for j in range(m):
        if g[i][j] != '^':
            dp[i][j] = dp[i-1][j]
            if j < m-1 and g[i][j+1] == '^':
                dp[i][j] += dp[i-1][j+1]
            if j > 0 and g[i][j-1] == '^':
                dp[i][j] += dp[i-1][j-1]
ans2 = sum(dp[-1])
print(ans2)