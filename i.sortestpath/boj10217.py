from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = 1000000000
T = int(input())

def dijkstra(st):
    dist = [[ INF ] * (M+1) for _ in range(N)]
    dist[st][0] = 0

    q = [(0, st, 0)]
    while q:
        curd, curv, curc = heappop(q)

        if curd > dist[curv][curc]: continue

        for (nv, nd, nc) in edges[curv]:
            newd = nd+curd
            newc = nc+curc
            if newc <= M and dist[nv][newc] > newd:
                for j in range(newc+1, M+1):
                    if dist[nv][j] <= newd: break
                    dist[nv][j] = newd

                dist[nv][newc] = newd
                heappush(q, (newd, nv, newc))
    return dist

def testcase():
    global N, M, edges
    N, M, K = map(int, input().split())
    edges = [[] for _ in range(N)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        edges[u-1].append((v-1, d, c))

    cost = dijkstra(0)
    minc = min(cost[N-1])
    if minc == 1000000000:
        print("Poor KCM")
    else:
        print(minc)

for _ in range(T):
    testcase()
    