import sys
input = sys.stdin.readline



def gogo(a, b, x, y, dd):
    return dd[x][y] - dd[x][b-1] - dd[a-1][y] + dd[a-1][b-1]


N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
dd = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dd[i+1][j+1] = dd[i][j+1] + dd[i+1][j] + jido[i][j] - dd[i][j]


for _ in range(M):
    print(gogo(*list(map(int, input().split())), dd))