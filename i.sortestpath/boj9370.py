"""
미확인 도착지
단일-출발 최단 경로 문제
"""
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(st):
    dist = [ 97654321 ] * n
    dist[st] = 0

    q = [(0, st)]
    while q:
        curd, curv = heappop(q)

        if curd > dist[curv]: continue
        for (nv, nd) in E[curv]:
            new_d = curd + nd
            if new_d < dist[nv]:
                dist[nv] = new_d
                heappush(q, (new_d, nv))
    return dist

def testcase():
    global n, E
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    E = [[] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        E[a-1].append((b-1, d))
        E[b-1].append((a-1, d))

    hubos = [ int(input()) for _ in range(t) ]

    sdij = dijkstra(s-1)
    gdij = dijkstra(g-1)
    hdij = dijkstra(h-1)
    result = []
    for hubo in hubos:
        dd = min(sdij[g-1]+gdij[h-1]+hdij[hubo-1],
                    sdij[h-1]+hdij[g-1]+gdij[hubo-1])
        if sdij[hubo-1] == dd:
            result.append(hubo)
    print(' '.join([str(i) for i in sorted(result)]))

T = int(input())
for _ in range(T):
    testcase()