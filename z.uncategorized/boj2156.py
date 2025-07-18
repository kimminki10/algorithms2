import sys
input = sys.stdin.readline

n = int(input())
d = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    cur = int(input())
    d[i][0] += max(d[i-1])
    d[i][1] += d[i-1][0] + cur
    d[i][2] += d[i-1][1] + cur

print(max(d[n]))