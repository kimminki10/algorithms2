import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def bfind(arr, v):
    l = 0; r = len(arr)-1; m = ans = 0
    while l <= r:
        m = (l+r) // 2
        if arr[m] < v:
            l = m+1
        else:
            ans = m
            r = m-1
    return ans

def lis(arr):
    l = [arr[0]]
    for i in arr[1:]:
        if l[-1] < i: l.append(i)
        else:
            bi = bfind(l, i)
            l[bi] = i
    return l

print(len(lis(A)))
