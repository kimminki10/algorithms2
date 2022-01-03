"""
양팔저울
"""

import sys
input = sys.stdin.readline

N = int(input())
chu = [*map(int, input().split())]
gu_num = int(input())
gu = [*map(int, input().split())]

d = {}
for c in chu:
    d_keys = list(d.keys())
    for k in d_keys:
        d[c+k] = True
        d[abs(c - k)] = True
    d[c] = True

result = []
for g in gu:
    if g in d.keys():
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))