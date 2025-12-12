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

FN = "input/11.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
lines = FILE.read().strip().split("\n")

adj = {}
for line in lines:
    u, vv = line.split(": ")
    adj[u] = vv.split(" ")

@cache
def dfs1(u):
    if u == "out":
        return 1
    ans = 0
    for v in adj.get(u, []):
        ans += dfs1(v)
    return ans

@cache
def dfs2(u, dac=False, fft=False):
    if u == "out" and dac and fft:
        return 1
    ans = 0
    for v in adj.get(u, []):
        ans += dfs2(v, dac or v == "dac", fft or v == "fft")
    return ans

ans1 = dfs1("you")
ans2 = dfs2("svr")

print(ans1)
print(ans2)
