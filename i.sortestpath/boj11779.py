from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = 987654321
n = int(input())
m = int(input())

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1, c))

def dijkstra(start):
    dist = [ INF ] * n
    prev = [ -1 ] * n

    dist[start] = 0
    
    q = [ (0, start) ]
    while q:
        d, c = heappop(q)

        if dist[c] < d: continue
        for (nv, nd) in edges[c]:
            newd = nd + d
            if newd < dist[nv]:
                dist[nv] = newd
                prev[nv] = c
                heappush(q, (newd, nv))

    return dist, prev

st, en = map(int, input().split())

dd, pp = dijkstra(st-1)
cities = []
count  = 0
cur = en-1
while cur != -1:
    count += 1
    cities.append(cur)
    cur = pp[cur]

print(dd[en-1])
print(count)
print(' '.join([str(i+1) for i in reversed(cities)]))