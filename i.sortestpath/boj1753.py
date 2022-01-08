"""
최단경로
"""

import sys
input = sys.stdin.readline

from queue import PriorityQueue


def dijkstra(s, v_num, g):
    dist = [ 987654321 for _ in range(v_num) ]
    dist[s] = 0

    pq = PriorityQueue()
    pq.put([0, s])
    while not pq.empty():
        c = pq.get()
        curV = c[1]
        cost = c[0]

        if dist[curV] < cost: continue
        if not curV in g.keys(): continue
        for v in g[curV]:
            neighbor = v[0]
            neighbor_dist = v[1] + cost
            if dist[neighbor] > neighbor_dist:
                dist[neighbor] = neighbor_dist
                pq.put([neighbor_dist, neighbor])
    return dist

V, E = map(int, input().split())
K = int(input())

g = {}
for _ in range(E):
    u, v, w = map(int, input().split())
    if u in g.keys():
        g[u].append([v, w])
    else:
        g[u] = [[v, w]]

result = dijkstra(K, V+1, g)
print(result)
for r in result[1:]:
    if r == 987654321:
        print("INF")
    else:
        print(r)