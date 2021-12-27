"""
boj.kr/11053
가장 긴 증가하는 부분 수열
lis length
"""

import sys
input = sys.stdin.readline

def lis_length(n, arr):
    d = [ 0 for _ in range(n) ]

    for i, v in enumerate(arr):
        d[i] = 1
        for j in range(i):
            if arr[j] < v and d[i] < d[j] + 1:
                d[i] = d[j] + 1

    return max(d)


def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    print(lis_length(N, arr))


solve()