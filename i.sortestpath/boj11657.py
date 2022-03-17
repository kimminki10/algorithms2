from cmath import inf
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A-1].append([B-1, C])

minus_cycle = False
distance = [ inf for _ in range(N) ]
distance[0] = 0
for i in range(N):
    for j in range(N):
        for p in edges[j]:
            next, d = p
            if distance[j] != inf and distance[next] > distance[j] + d:
                distance[next] = distance[j] + d
                if i == N-1:
                    minus_cycle = True

if minus_cycle:
    print(-1)
else:
    for i in range(1, N):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])