from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().strip())
d = defaultdict(lambda: 0)

for _ in range(N):
    l = " ".join(sorted(input().split()))
    d[l] += 1

print(max(d.values()))