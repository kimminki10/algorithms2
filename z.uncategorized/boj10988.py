import sys
input = sys.stdin.readline

def is_palin(s):
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            return 0
    return 1

print(is_palin(input().strip()))