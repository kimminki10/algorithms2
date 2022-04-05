import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))

minv = 9876543211
minc = ()
l = 0; r = N-1
while l < r:
    s = arr[l] + arr[r]
    asum = abs(s)
    if minv > asum:
        minv = asum
        minc = (l, r)
    if s < 0:
        l += 1
    elif s > 0:
        r -= 1
    elif s == 0:
        break

print(' '.join([str(arr[i]) for i in minc]))