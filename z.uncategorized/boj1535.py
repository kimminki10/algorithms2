import sys
input = sys.stdin.readline

N = int(input()) # N <= 20
W = list(map(int,input().split()))
V = list(map(int,input().split()))
M = 100

d = [[0] * (N+1) for _ in range(102)]

for j in range(1, N+1):
    w, v = W[j-1], V[j-1]
    for i in range(M+1):
        if i < w:
            d[i][j] = d[i][j-1]
        else:
            d[i][j] = max(v+d[i-w][j-1], d[i][j-1])

print(d[M-1][N])