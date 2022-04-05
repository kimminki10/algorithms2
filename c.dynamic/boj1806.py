import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

l = 0; r = 0
s = 0
minl = 987654321

while r <= N:
    if s < S:
        if r < N:
            s += arr[r]
        r += 1
    else:
        lr = r-l
        if minl > lr:
            minl =lr
        s -= arr[l]
        l += 1

if minl == 987654321:
    print(0)
else:
    print(minl)