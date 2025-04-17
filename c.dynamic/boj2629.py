import sys
input = sys.stdin.readline

N = int(input()) # N <= 30
A = list(map(int, input().split()))
M = int(input()) # M <= 7
check = list(map(int,input().split()))

d = set()
d.add(0)
for a in A:
    for k in list(d):
        d.add(abs(k-a))
        d.add(a+k)

print(' '.join([ "Y" if c in d else "N" for c in check]))
        