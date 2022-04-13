import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def bisect_left(arr, v):
    l = 0; r = len(arr) - 1; m = ans = 0
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
    idxl = [0]
    for i in arr[1:]:
        if l[-1] < i: 
            idxl.append(len(l))
            l.append(i)
        else:
            bi = bisect_left(l, i)
            l[bi] = i
            idxl.append(bi)
    return l, idxl

l, idxl = lis(A)
llen = len(l)

re_lis = []
find_idx = llen-1
for i in range(N-1, -1, -1):
    if idxl[i] == find_idx:
        re_lis.append(A[i])
        find_idx -= 1

print(llen)
print(' '.join(list(str(i) for i in reversed(re_lis))))

