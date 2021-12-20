"""
https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=581
택배 마스터 광우
큐, 순열
"""

import sys
input = sys.stdin.readline

import itertools

N, M, K = map(int, input().split())
arr = map(int, input().split())
result = 987654321

def dojob(k, p, m):
    global result
    part_sum = 0
    s = 0
    i = 0
    while True:
        if part_sum > result: return
        if k == 0: break

        if s + p[i] <= m:
            s += p[i]
        else:
            part_sum += s
            s = p[i]
            k -= 1
        i = (i + 1) % N


    if part_sum < result:
        result = part_sum

def solve():
    for p in itertools.permutations(arr):
        dojob(K, p, M)
    print(result)

solve()