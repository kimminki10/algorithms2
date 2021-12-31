"""
https://www.acmicpc.net/problem/13305
주유소
greedy
"""

import sys
input = sys.stdin.readline

N = int(input())
V = list(map(int, input().split()))
E = list(map(int, input().split()))

min_gas = E[0]
cost = 0
for v, e in zip(V, E[1:]):
    cost += min_gas * v
    if e < min_gas: min_gas = e
    
print(cost)