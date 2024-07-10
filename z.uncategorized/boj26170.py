import sys
input = sys.stdin.readline

di = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs(r,c, jido) -> int:
    q = [[r,c, jido[r][c], {(r,c)}]]
    while q:
        a,b,s,d = q.pop(0)
        for x, y in di:
            nx, ny = a+x, b+y
            if 0 <= nx < 5 and 0 <= ny < 5 and jido[nx][ny] != -1 and (nx,ny) not in d:
                ns = s+jido[nx][ny]
                if ns == 3: return len(d)
                q.append([nx,ny,ns, d|{(nx,ny)}])
    return -1


jido = [list(map(int, input().split())) for _ in range(5)]
r,c = map(int, input().split())

print(bfs(r, c, jido))