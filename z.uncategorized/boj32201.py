import sys
input = sys.stdin.readline

N = int(input())
A = { v: i for i, v in enumerate(input().split()) }
arr = []
best = 0
for i, v in enumerate(input().split()):
    diff = A[v]-i
    if diff > best:
        best = diff
        arr = []
    if diff == best: arr.append(v)

print(" ".join(arr))
    