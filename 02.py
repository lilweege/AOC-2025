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

FN = "input/02.txt"
# FN = "sample.txt"

FILE = open(FN, "r")

s = FILE.read().strip()

ans1 = ans2 = 0
for a, b in [map(int, p.split("-")) for p in s.split(",")]:
    for x in range(a, b+1):
        s = str(x)
        n = len(s)
        if n & 1 == 0 and s[n//2:] == s[:n//2]:
            ans1 += x
        for i in range(1, n):
            if n % i == 0 and s.count(s[:i]) == n // i:
                ans2 += x
                break

print(ans1)
print(ans2)