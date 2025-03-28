from bisect import bisect_left
import sys
input = sys.stdin.readline


def testcase():
    N = int(input()) # 40000
    arr = []
    for _ in range(N):
        print(arr)
        num = int(input())
        if not arr or arr[-1] < num:
            arr.append(num)
        else:
            idx = bisect_left(arr, num)
            arr[idx] = num
    print(arr)
    return len(arr)


def solve():
    T = int(input())
    for _ in range(T):
        res = testcase()
        print(res)


solve()