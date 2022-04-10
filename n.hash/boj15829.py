import sys
input = sys.stdin.readline

BASE = 31
MOD = 1234567891
N = int(input().rstrip())
line = input().rstrip()

def sn(c):
    return ord(c) - ord('a') + 1

def hash_func(s, n):
    s = s[::-1]
    h = 0
    for i in range(n-1):
        h = ((h + sn(s[i])) * BASE) % MOD
    h += sn(s[n-1])
    return h % MOD

print(hash_func(line, N))