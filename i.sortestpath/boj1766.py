from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B-1] += 1
    edges[A-1].append(B-1)

result = [0] * N
q = []
for i in range(N):
    if indegree[i] == 0:
        q.append(i)

for i in range(N):
    if q:
        cur = heappop(q)

        result[i] = cur+1

        for next in edges[cur]:
            indegree[next] -= 1

            if indegree[next] == 0: heappush(q, next)

print(' '.join([str(i) for i in result]))