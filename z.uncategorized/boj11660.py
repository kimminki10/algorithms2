import sys
input = sys.stdin.readline

def subsum2(a,b,x,y,d):
    return d[x][y] - d[x][b-1]-d[a-1][y]+d[a-1][b-1]

N,M = map(int,input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        d[i][j] = d[i][j-1] + d[i-1][j] + jido[i-1][j-1] - d[i-1][j-1]

for _ in range(M):
    a,b,x,y = map(int,input().split())
    print(subsum2(a,b,x,y,d))