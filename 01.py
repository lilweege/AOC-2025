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

FN = "input/01.txt"
# FN = "sample.txt"

FILE = open(FN, "r")

s = FILE.read().strip()
lines = s.split("\n")

ans1 = ans2 = 0
pos = 50
for line in lines:
    line = line.split()[0]
    d = line[0]
    x = int(line[1:])
    if d == 'L':
        x = -x
    ppos = pos
    pos += x
    if pos < 0:
        pos += 100
        ppos += 100
    ans2 += abs(pos // 100 - ppos // 100) - (ppos % 100 == 0 if d == 'L' else pos % 100 == 0)
    if pos % 100 == 0:
        ans1 += 1
        ans2 += 1

print(ans1)
print(ans2)