from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = 987654321
N = int(input())
M = int(input())
edges = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1,c))

def dijkstra(start):
    result = [ INF ] * N
    result[start] = 0

    q = [(0, start)]
    while q:
        d, v = heappop(q)

        if result[v] < d: continue
        for e, new_d in edges[v]:
            dd = new_d+d
            if result[e] > dd:
                result[e] = dd
                heappush(q, (dd, e))
    return result

st, en = map(int, input().split())
print(dijkstra(st-1)[en-1])