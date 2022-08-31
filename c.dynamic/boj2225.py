import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(N+1):
    dp[1][i] = 1

for i in range(1, K+1):
    for j in range(N+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= 1_000_000_000

print(dp[K][N])