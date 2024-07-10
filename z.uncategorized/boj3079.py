import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = sorted([ int(input().strip()) for _ in range(N) ])

def is_possible(m):
    left = M
    for i in T:
        left -= m // i
    return left <= 0


def binary():
    l = 0
    r = M * T[-1]
    m = (l+r)//2
    ans = m

    while l<=r:
        m = (l+r)//2
        if is_possible(m):
            ans = m
            r = m-1
        else:
            l = m+1
    return ans

print(binary())