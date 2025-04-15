import sys
input = sys.stdin.readline

N = int(input())
d = [0] * 100_005
for _ in range(N):
    a = int(input())
    d[a] = max(d[:a]) + a

print(max(d))