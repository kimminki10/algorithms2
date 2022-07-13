import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 ** 14)

N = int(input().rstrip())
T = []
P = []
for _ in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [ 0 ] * 20
for i in range(N):
    if i + T[i] <= N and dp[i] + P[i] > dp[i+T[i]]:
        dp[i+T[i]] = dp[i] + P[i]
    dp[i+1] = max(dp[i], dp[i+1])


print(dp[N])