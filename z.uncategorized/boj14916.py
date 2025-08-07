import sys
input = sys.stdin.readline

n = int(input())
ans = -1
for i in range(n//5,-1,-1):
    cur = n - 5*i
    if cur % 2 == 0:
        ans = i + cur//2
        break
print(ans)