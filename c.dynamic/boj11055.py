import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

def bis(arr):
    d = [0] * N

    for i, v in enumerate(A):
        d[i] = arr[i]
        for j in range(i):
            if arr[j] < v and d[i] < d[j] + v:
                d[i] = d[j] + v

    return d

print(max(bis(A)))