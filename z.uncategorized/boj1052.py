import sys
sys.setrecursionlimit(2**14)
input = sys.stdin.readline

N, K = map(int, input().split())

t = 1
while t < N: t *= 2

def gogo(t, n, k):
    if n <= k:
        return 0
    if k == 1:
        a = 1
        while a < n: a *= 2
        return a - n
    
    while t > n: t //= 2
    return gogo(t, n-t, k-1)

print(gogo(t, N, K))