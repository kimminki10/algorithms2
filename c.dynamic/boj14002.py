import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def lis(arr):
    d = [ 0 ] * N
    l = [[] for _ in range(N)]

    for i, v in enumerate(arr):
        d[i] = 1
        l[i].append(v)
        for j in range(i):
            if arr[j] < v and d[i] < d[j] + 1:
                l[i].clear()
                l[i] = l[j][:]
                l[i].append(arr[i])
                d[i] = d[j]+1
    result = l[0]
    for i in l:
        if len(result) < len(i):
            result = i
    return result

l = lis(A)
print(len(l))
print(' '.join([str(i) for i in l]))