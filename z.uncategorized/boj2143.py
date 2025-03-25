from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def solve(T, N, A, M, B):
    def subsum(arr):
        res = [0]
        for v in arr:
            res.append(res[-1] + v)
        return res

    SA = subsum(A) # N
    SB = subsum(B) # N

    DA = defaultdict(int)
    DB = defaultdict(int)

    answer = 0
    # N^2
    for i in range(1, N+1):
        for j in range(i):
            diff = SA[i] - SA[j]
            DA[diff] += 1
    # M^2
    for i in range(1, M+1):
        for j in range(i):
            diff = SB[i] - SB[j]
            DB[diff] += 1

    for k in DA.keys():
        if T - k in DB:
            answer += DA[k] * DB[T - k]
    return answer


T = int(input()) # -10^9 <= T <= 10^9
N = int(input()) # 1000
A = list(map(int, input().split())) # -10^6 <= A[i] <= 10^6
M = int(input()) # 1000
B = list(map(int, input().split())) # -10^6 <= B[i] <= 10^6
print(solve(T, N, A, M, B))