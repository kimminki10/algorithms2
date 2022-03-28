from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
item_num = [int(i) for i in input().split()]

edges = [[] for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1, c))
    edges[b-1].append((a-1, c))

def dijkstra(start):
    dist = [987654321] * n
    dist[start] = 0
    
    q = [(0, start)]
    while q:
        cd, cv = q.pop(0)

        if dist[cv] < cd: continue
        for (nv, nd) in edges[cv]:
            newd = nd+cd
            if dist[nv] > newd:
                dist[nv] = newd
                heappush(q, (newd, nv))

    return dist

answer = 0
for i in range(n):
    dist = dijkstra(i)
    answer = max(answer, sum([item_num[i] for i, v in enumerate(dist) if v <= m]))
print(answer)