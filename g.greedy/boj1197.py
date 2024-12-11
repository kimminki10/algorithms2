from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [[] for _ in range(V)]
for _ in range(E):
    a,b,c = map(int, input().split())
    edges[a-1].append([c,b-1])
    edges[b-1].append([c,a-1])

visited = [False] * V
def prim(cur):
    ret = 0
    to_search = edges[cur]
    visited[cur] = True
    heapify(to_search)

    while to_search:
        c, n = heappop(to_search)
        if visited[n]: continue
        visited[n] = True
        
        ret += c
        for item in edges[n]:
            heappush(to_search, item)
    return ret

ans = 0
for i in range(V):
    if visited[i]: continue
    ans += prim(i)
print(ans)