from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [map(int, input().split()) for i in range(N)]
d = defaultdict(lambda: 0)
for s, y in arr:
    d[(s,y)] += 1
ans = 0
for r in d.values():
    ans += 1 + (r-1) // K
print(ans)