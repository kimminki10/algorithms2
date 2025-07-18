from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def lis_length(arr):
    brr = []
    for v in arr:
        if not brr or brr[-1] < v:
            brr.append(v)
        else:
            i = bisect_left(brr, v)
            brr[i] = v
    return len(brr)

print(lis_length(arr[::-1]))