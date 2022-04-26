import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sarr = [0]
s = 0
for i in arr:
    s += i
    sarr.append(s)

maxv = sarr[K] - sarr[0]
for i in range(K, N+1):
    cur = sarr[i] - sarr[i-K]
    if maxv < cur:
        maxv = cur
print(maxv)