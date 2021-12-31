"""
https://www.acmicpc.net/problem/11444
피보나치 수 6
수학
    n
1 1    =  F(n+1)  F(n)
1 0       F(n)    F(n-1)
분할정복
"""

import sys
input = sys.stdin.readline
from copy import deepcopy


N = int(input())
a = [[1, 1], [1, 0]]

def matmul(a, b):
    zip_b = list(zip(*b))
    return [ [ sum( ea*eb for ea, eb in zip(row_a, col_b)) % 1000000007 for col_b in zip_b] for row_a in a ]

def dac(s, n):
    if n == 1: return s
    
    arr = dac(s, n//2)
    cal = matmul(arr, arr)
    result = cal
    if n % 2:
        result = matmul(cal, a)
    return result

print(dac(a, N)[0][1])
