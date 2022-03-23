from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = 987654321
N, M, X = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a-1].append([b-1, t])

def dijkstra(start):
    result = [ INF ] * N
    result[start] = 0

    q = [(0, start)]
    while q:
        d, v = heappop(q)

        for e, new_d in edges[v]:
            if result[e] > new_d+d:
                result[e] = new_d+d
                heappush(q, (new_d+d, e))

    return result


goX = [ dijkstra(i)[X-1] for i in range(N) ]
gohome = dijkstra(X-1)

print(max([goX[i] + gohome[i] for i in range(N)]))