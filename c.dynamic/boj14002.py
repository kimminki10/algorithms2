from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def lis(arr):
    brr = []
    l = []
    for v in arr:
        if not brr or brr[-1] < v:
            l.append(len(brr))
            brr.append(v)
        else:
            i = bisect_left(brr, v)
            l.append(i)
            brr[i] = v
    bi = len(brr)-1
    ans = [0] * len(brr)
    for i in range(N-1,-1,-1):
        if l[i] == bi:
            ans[l[i]] = arr[i]
            bi -= 1
    return ans


ans = lis(arr)
print(len(ans))
print(' '.join(map(str, ans)))