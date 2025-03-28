from bisect import bisect_left
import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()

    brr = []
    for [_,y] in arr:
        if not brr or brr[-1] < y:
            brr.append(y)
        else:
            idx = bisect_left(brr, y)
            brr[idx] = y
    print(N - len(brr))
solve()