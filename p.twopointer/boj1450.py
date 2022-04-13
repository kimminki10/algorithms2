from bisect import bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
W = list(map(int, input().split()))

def possible_weight(arr):
    ret = []
    for i in range(len(arr)+1):
        for c in combinations(arr, i):
            ret.append(sum(c))
    return ret

def target_weight(left, right, v):
    right = list(sorted(right))
    ret = 0
    for l in left:
        bi = bisect_right(right, v-l)
        ret += bi
    print(ret)

m = N // 2
left = possible_weight(W[:m])
right = possible_weight(W[m:])

target_weight(left, right, C)