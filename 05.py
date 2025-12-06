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

FN = "input/05.txt"
# FN = "sample.txt"

FILE = open(FN, "r")

s = FILE.read().strip()

parts = s.split("\n\n")
intervals = [tuple(map(int, p.split("-"))) for p in parts[0].split("\n")]
queries = list(map(int, parts[1].split("\n")))
ans1 = 0
for q in queries:
    for a, b in intervals:
        if a <= q <= b:
            ans1 += 1
            break
print(ans1)

intervals.sort()
n = len(intervals)
s1, e1 = intervals[0]
ans2 = 0
for i in range(1, n):
    s2, e2 = intervals[i]
    if s2 <= e1+1:
        e1 = max(e1, e2)
    else:
        ans2 += e1 - s1 + 1
        s1, e1 = s2, e2
ans2 += e1 - s1 + 1
print(ans2)