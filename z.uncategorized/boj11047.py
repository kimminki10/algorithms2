import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
left = K
ans = 0
for v in A[::-1]:
    if v > left: continue
    ans += left // v
    left = left %  v

print(ans)