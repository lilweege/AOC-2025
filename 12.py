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

FN = "input/12.txt"
# FN = "sample.txt"

FILE = open(FN, "r")
content = FILE.read().strip()

*presents, regions = content.split("\n\n")
shapes = [shape.split("\n")[1:] for shape in presents]
n = len(shapes)
sizes = [sum(r.count("#") for r in shape) for shape in shapes]

ans = 0
for line in regions.split("\n"):
    wh, vals = line.split(": ")
    w, h = map(int, wh.split("x"))
    area = w * h
    need = list(map(int, vals.split(" ")))
    alwaysPossible = 9 * sum(need)
    exactNeed = sum(sizes[i] * x for i, x in enumerate(need))
    if area >= alwaysPossible:
        ans += 1
    elif area < exactNeed:
        # Even with a perfect packing this is impossible
        pass
    else:
        # This assertion never hits...
        # Worst problem ever?
        assert False, "Too hard"

print(ans)

'''
Some tilings of single shapes for my input, it's pretty tight

0:
###.###.###
############
############
.###.###.###


1:
###.###.###.
.############
############.
..###.###.###

2:
###.###.###..
.############
############.
..###.###.###

3:
########
########
########

4:
#####
##.##
#####

5:
#####.
######
.#####

'''