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

FN = "input/03.txt"
# FN = "sample.txt"

FILE = open(FN, "r")

s = FILE.read().strip()
lines = s.split("\n")

def solve(seqLen):
    ans = 0
    for line in lines:
        n = len(line)
        digs = [0] * seqLen
        for i in range(n):
            dig = int(line[i])
            for j in range(seqLen):
                if dig > digs[j] and i < n-seqLen+j+1:
                    digs[j] = dig
                    for k in range(j+1, seqLen):
                        digs[k] = 0
                    break
        x = 0
        for dig in digs:
            x = x * 10 + dig
        ans += x
    return ans

print(solve(2))
print(solve(12))
