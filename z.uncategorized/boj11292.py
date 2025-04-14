import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0: break
    arr = []
    maxh = 0
    for _ in range(N):
        name, h = input().split()
        h = float(h)
        if h == maxh: arr.append(name)
        elif h > maxh: 
            arr = [name]
            maxh = h
    print(' '.join(arr))