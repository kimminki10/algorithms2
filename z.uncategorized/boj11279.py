from heapq import heappush
from heapq import heappop

import sys
input = sys.stdin.readline


N = int(input().strip())
arr = []

for _ in range(N):
    v = int(input().strip())
    if v == 0:
        print(-heappop(arr) if arr else 0)
    else:
        heappush(arr, -v)
