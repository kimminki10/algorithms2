import sys
input = sys.stdin.readline

N = int(input())
dmax = [0,0,0]
dmin = [0,0,0]

for i in range(1, N+1):
    lines = list(map(int, input().split()))
    a = lines[0] + max(dmax[0], dmax[1])
    b = lines[1] + max(dmax[0], dmax[1], dmax[2])
    c = lines[2] + max(dmax[1], dmax[2])
    dmax = [a, b, c]

    a = lines[0] + min(dmin[0], dmin[1])
    b = lines[1] + min(dmin[0], dmin[1], dmin[2])
    c = lines[2] + min(dmin[1], dmin[2])
    dmin = [a, b, c]
    
print(max(dmax), min(dmin))