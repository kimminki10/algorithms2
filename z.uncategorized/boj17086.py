from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jido = [ list(map(int, input().split())) for _ in range(N)]
di = [[1,0],[0,1],[1,1],[-1,-1],
      [-1,0],[0,-1],[1,-1],[-1,1]]

def bfs(sx,sy):
    q = deque()
    q.append([sx,sy, 0])
    visit = set()
    visit.add((sx,sy))

    while q:
        x,y,l = q.popleft()

        for dx,dy in di:
            nx,ny = dx+x,dy+y
            if 0 <= nx < N and 0 <= ny < M:
                if jido[nx][ny] == 1:
                    return l+1
                elif (nx,ny) not in visit:
                    visit.add((nx,ny))
                    q.append([nx,ny,l+1])
    return -1


ans = 0
for x in range(N):
    for y in range(M):
        if jido[x][y] == 0:
            ans = max(ans, bfs(x,y))

print(ans)