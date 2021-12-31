"""
행렬 곱셈
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [ [ int(i) for i in input().split() ] for _ in range(N) ]
_, K = map(int, input().split())
B = [ [ int(i) for i in input().split() ] for _ in range(M) ]

def mat_mul(a, b):
    zip_b = list(zip(*b)) # transitive b
    return [ [ sum( ea*eb for ea, eb in zip(row_a, col_b) ) for col_b in zip_b] for row_a in a ]

def print_mul(a):
    for row in a:
        print(' '.join(map(str,row)))
print_mul(mat_mul(A, B))
