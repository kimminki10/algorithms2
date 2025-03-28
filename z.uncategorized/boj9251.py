import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

dp = [0] * max(len(A), len(B))
for a in A:
    m = 0
    for j, b in enumerate(B):
        if m < dp[j]:
            m = dp[j]
            continue
        if a == b:
            dp[j] = m + 1

print(max(dp))