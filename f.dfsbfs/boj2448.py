import sys
sys.setrecursionlimit(2 ** 14)
input = sys.stdin.readline

N = int(input())
height = N
width = height * 2
paper =[ [' '] * width for _ in range(height) ]

def printStar(sx, sy, ex, ey):
    for x in range(ex-1, sx-1, -1):
        for y in range(ex-x-1+ sy, ey-1, ex-x):
            paper[x][y] = '*'

def dfs(sx, sy, ex, ey):
    if ey - sy <= 6:
        printStar(sx,sy,ex,ey)
        return
    
    mx = (sx + ex) // 2
    my = (sy + ey) // 2
    qy = (ey - sy) // 4
    dfs(mx, sy, ex, my)
    dfs(mx, my, ex, ey)
    dfs(sx, my-qy, mx, my+qy)

dfs(0, 0, height, width)

for r in paper:
    print(''.join(r))