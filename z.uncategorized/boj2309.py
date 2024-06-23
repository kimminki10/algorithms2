from itertools import permutations

import sys
input = sys.stdin.readline

def sumsum(l, perm):
    result = 0
    for i in perm:
        result += l[i]
    return result

def printprint(l, perm):
    for i in perm:
        print(l[i])

arr = sorted([int(input()) for _ in range(9)])
for perm in permutations(range(9), 7):
    s = sumsum(arr, perm)
    if s == 100:
        printprint(arr, perm)
        break