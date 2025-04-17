import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [ list(map(int,input().split())) for _ in range(N) ]

d = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    sw, sv = arr[i-1]
    for j in range(K+1):
        if j < sw:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], sv + d[i-1][j-sw])
print(d[N][K])