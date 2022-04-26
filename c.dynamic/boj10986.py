from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = map(int, input().split())
sarr = []

s = 0
for v in arr:
    s += v
    sarr.append(s)

h = defaultdict(lambda: 0)
for v in sarr:
    h[v % M] += 1

ret = h[0]
for (k, v) in h.items():
    now = v
    ret += now * (now - 1) // 2

print(ret)