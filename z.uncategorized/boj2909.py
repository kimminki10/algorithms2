import sys
input = sys.stdin.readline

c, k = map(int,input().split())
d = 10**k

print((c+d//2)//d * d)