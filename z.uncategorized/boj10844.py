import sys
input = sys.stdin.readline

N = int(input())
divisor = 1_000_000_000

d = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, N+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]
    for j in range(1, 9):
        d[i][j] = (d[i][j]+d[i-1][j-1]) % divisor
        d[i][j] = (d[i][j]+d[i-1][j+1]) % divisor

print(sum(d[N]) % divisor)