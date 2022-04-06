import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

minv = 9876543211
minc = (0,0)
l=0;r=N-1
while l < r:
    s = arr[l] + arr[r]
    asum = abs(s)
    if asum < minv:
        minv = asum
        minc = (l, r)

    if s > 0:
        r -= 1
    else:
        l += 1

print(' '.join([str(arr[i]) for i in minc]))