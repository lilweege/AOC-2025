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

FN = "input/06.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
lines = FILE.read().split("\n")
lines[-1].strip()
if len(lines[-1]) == 0:
    lines.pop()
*first, last = lines

f = {
    "+": int.__add__,
    "*": int.__mul__,
}


def part1():
    g = zip(*(map(int, re.split(r"\s+", line.strip())) for line in first))
    ops = map(f.get, re.split(r"\s+", last))
    return sum(reduce(op, nums) for op, nums in zip(ops, g))


def part2():
    n = len(first[0])
    m = len(first)
    ans = acc = 0
    op = f[last[0]]
    for i in range(n):
        x = 0
        for j in range(m):
            c = first[j][i]
            if c != ' ':
                x = x * 10 + int(c)
        if x == 0: continue
        if last[i] == ' ':
            acc = op(acc, x)
        else:
            ans += acc
            acc = x
            op = f[last[i]]
    ans += acc
    return ans


print(part1())
print(part2())