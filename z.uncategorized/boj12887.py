import sys
input = sys.stdin.readline

M = int(input())
jido = [ [*input().strip()] for _ in range(2) ]
di = [[0,1], [1,0], [-1,0]]

count = 0
for i in range(2):
    for j in range(M):
        if jido[i][j] == '.':
            count += 1

start_row = 0
for v in range(M):
    if jido[0][v] == '#':
        start_row = 1
        break
    if jido[1][v] == '#':
        start_row = 0
        break

def bfs(sx,sy):
    if jido[sx][sy] == '#':
        return 0

    q = [[sx,sy,0]]
    while q:
        x,y,d = q.pop(0)

        if y == M-1:
            return count-d-1

        for a,b in di:
            nx,ny = x+a,y+b
            if 0<=nx<2 and 0<=ny<M and jido[nx][ny]=='.':
                jido[nx][ny] = '#'
                q.append([nx,ny,d+1])

print(bfs(start_row,0))