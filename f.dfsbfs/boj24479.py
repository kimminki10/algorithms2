import sys
sys.setrecursionlimit(2 ** 17)
input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [0] * N
vidx = 1

edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

for row in edges:
    row.sort()

def dfs(R):
    global visited, vidx
    visited[R] = vidx
    vidx += 1
    for x in edges[R]:
        if visited[x] == 0:
            dfs(x)

dfs(R-1)
for i in range(N):
    print(visited[i])