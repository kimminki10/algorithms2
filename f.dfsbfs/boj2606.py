"""
바이러스
"""

import sys
input = sys.stdin.readline

N = int(input())
E_num = int(input())

arr = [*range(N+1)]

def find(v):
    if arr[v] == v:
        return v
    arr[v] = find(arr[v])
    return arr[v]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root: return

    for i in range(1, N+1):
        if arr[i] == b_root:
            arr[i] = a_root
    
for _ in range(E_num):
    a, b = map(int, input().split())
    union(a, b)

ones_root = find(1)
print(arr.count(ones_root)-1)