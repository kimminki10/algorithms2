import sys
import functools
input = sys.stdin.readline

n, m = list(map(int, input().split()))

@functools.lru_cache
def ncm_num(n, m):
    if m == n or m == 0:
        return 1
    return ncm_num(n-1, m-1) + ncm_num(n-1, m)

print(ncm_num(n,m))