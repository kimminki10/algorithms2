import sys
input = sys.stdin.readline

N = int(input().strip())
P = [ int(i) for i in input().split() ]
d = [0] + [987654321] * 1001

for i in range(1, N+1):
    for j in range(1, i+1):
        d[i] = min(d[i], d[i-j]+P[j-1])

print(d[N])