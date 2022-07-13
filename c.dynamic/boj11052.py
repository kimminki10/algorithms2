import sys
input = sys.stdin.readline


N = int(input().rstrip())
P = list(map(int, input().split()))


d = [0] * 1001
for i in range(1, N+1):
    d[i] = P[i-1]

for i in range(1, N+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j]+P[j-1])

print(d[N])