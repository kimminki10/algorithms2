from collections import defaultdict, deque
from functools import reduce
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
e = defaultdict(lambda:[])
for _ in range(M):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)


def gogo(start):
    q = deque()
    q.append([start, 0])
    res = [-1] * (N+1)
    res[start] = 0
    while q:
        cur, d = q.popleft()

        for n in e[cur]:
            if res[n] == -1:
                q.append((n, 1-d))
                res[n] = 1-d
            elif res[n] == d:
                return [-1]
    return res[1:]

res = gogo(1)
count = res.count(0) * res.count(1) * 2
print(count)