import sys
input = sys.stdin.readline

N = int(input())

d = [[0] * 3 for _ in range(N+1)]
C = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    d[i+1][0] = min(d[i][1], d[i][2]) + C[i][0]
    d[i+1][1] = min(d[i][0], d[i][2]) + C[i][1]
    d[i+1][2] = min(d[i][0], d[i][1]) + C[i][2]

print(min(d[N]))