import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = [[987654321] * n for _ in range(n)]
for i in range(n): edges[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a-1][b-1] = min(c, edges[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            edges[i][j] = min(edges[i][k]+edges[k][j], edges[i][j])

for i in range(n):
    for j in range(n):
        if edges[i][j] == 987654321:
            edges[i][j] = 0

for r in edges:
    for i in r:
        print(i, end=' ')
    print()