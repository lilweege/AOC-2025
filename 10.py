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

FN = "input/10.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
lines = FILE.read().strip().split("\n")

import z3

ans1 = ans2 = 0
for i, line in enumerate(lines):
    sLights, *sButtons, sJoltage = line.split(" ")
    lights = 0
    for c in reversed(sLights.strip("[]")):
        lights <<= 1
        if c == '#':
            lights |= 1

    buttons = [reduce(ior, map(lambda x: 1 << int(x), button.strip("()").split(","))) for button in sButtons]
    n = len(buttons)
    best = n
    for b in range(1, 1 << n):
        if b.bit_count() < best and lights == reduce(xor, (buttons[i] for i in range(n) if b & (1 << i))):
            best = b.bit_count()
    ans1 += best

    solver = z3.Optimize()

    joltage = tuple(map(int, sJoltage.strip("{}").split(",")))
    buttons = [tuple(map(int, button.strip("()").split(","))) for button in sButtons]
    n = len(joltage)
    m = len(buttons)
    counters = [z3.Int(f"counter_{i}") for i in range(n)]
    presses = [z3.Int(f"presses_{j}") for j in range(m)]
    for press in presses:
        solver.add(press >= 0)
    for i in range(n):
        add = []
        for j, button in enumerate(buttons):
            for counter in button:
                if counter == i:
                    add.append(presses[j])
                    break

        solver.add(z3.Sum(add) == joltage[i])

    solver.minimize(z3.Sum(presses))
    assert solver.check() == z3.sat
    ans = solver.model()
    ans2 += sum(ans[press].as_long() for press in presses)

print(ans1)
print(ans2)
