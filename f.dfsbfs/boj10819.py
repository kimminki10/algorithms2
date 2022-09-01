from itertools import permutations
import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))


def evaluate(p):
    res = 0
    for a, b in zip(p[:-1], p[1:]):
        res += abs(a-b)
    return res

A.sort()
answer = 0
for perm in permutations(A):
    answer = max(answer, evaluate(perm))

print(answer)