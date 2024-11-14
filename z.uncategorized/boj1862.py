import sys
input = sys.stdin.readline

n = input().rstrip()
m = list(map(int, '012356789'))
d = { v:i for i, v in enumerate(m) }

def change(n, m):
    ans = 0
    ml = len(m)
    nl = len(n)
    for i, v in enumerate(n):
        ans += d[int(v)] * (ml ** (nl-i-1))
    return ans

print(change(n, m))