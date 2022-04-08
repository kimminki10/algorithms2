import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def lis(arr):
    d = [ 0 ] * N

    for i, v in enumerate(arr):
        d[i] = 1
        for j in range(i):
            if arr[j] < v and d[i] < d[j] + 1:
                d[i] = d[j] + 1
    return d

print(max([ sum(i) for i in zip(lis(arr), lis(arr[::-1])[::-1])]) -1)