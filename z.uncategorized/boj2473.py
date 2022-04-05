import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))

minv = 9876543211
minc = None

for i in range(N):
    l = i+1; r = N-1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        asum = abs(s)
        if minv > asum:
            minv = asum
            minc = (arr[i], arr[l], arr[r])

        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            break
    else:
        continue
    break

print(' '.join([str(i) for i in minc]))