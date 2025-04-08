import sys
input = sys.stdin.readline

# 2sec

N, M = map(int, input().split())
di = [[-1,0],[0,1],[1,0],[0,-1]]
x,y,d = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

def is_clean(x,y):
    for i in range(4):
        if jido[x+di[i][0]][y+di[i][1]] == 0:
            return False
    return True

ans = 0
while True:
    if jido[x][y] == 0:
        jido[x][y] = 2
        ans += 1
    if is_clean(x,y):
        bd = (d + 2) % 4
        bx,by = di[bd]
        if jido[x+bx][y+by] == 1:
            break
        else:
            x += bx
            y += by
    else:
        d = (d-1) % 4
        dx,dy = di[d]
        if jido[x+dx][y+dy] == 0:
            x += dx
            y += dy
print(ans)