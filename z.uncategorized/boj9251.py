import sys
input = sys.stdin.readline


A = input().rstrip()
B = input().rstrip()
al = len(A)+1
bl = len(B)+1
dp = [[0] * al for _ in range(bl)]

for i in range(1, bl):
    for j in range(1, al):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if A[j-1] == B[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

print(dp[bl-1][al-1])
        