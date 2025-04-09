from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jido = list(list(map(int, input().split())) for _ in range(N))

CC = {
    1: [
        [[0,1]],
        [[1,0]],
        [[-1,0]],
        [[0,-1]]
    ],
    2: [
        [[1,0],[-1,0]],
        [[0,1],[0,-1]],
    ],
    3: [
        [[-1,0],[0,1]],
        [[1,0],[0,1]],
        [[1,0],[0,-1]],
        [[0,-1],[-1,0]],
    ],
    4: [
        [[0,1],[-1,0],[0,-1]],
        [[0,1],[1,0],[-1,0]],
        [[0,1],[1,0],[0,-1]],
        [[1,0],[-1,0],[0,-1]],
    ],
    5: [
        [[1,0],[0,1],[-1,0],[0,-1]]
    ]
}

p = []
for i in range(N):
    for j in range(M):
        if 1 <= jido[i][j] <= 5:
            p.append([i,j])


def gogo(x,y,di, jd):
    for d in di:
        nx,ny = x,y
        dx,dy = d
        while True:
            nx,ny = nx+dx,ny+dy
            if 0<=nx<N and 0<=ny<M and jd[nx][ny] != 6:
                if jd[nx][ny] == 0:
                    jd[nx][ny] = '#'
            else:
                break



ans = float('inf')
def dfs(arr, jd):
    global ans
    if not arr:
        t = 0
        for i in range(N):
            for j in range(M):
                if jd[i][j] == 0:
                    t += 1
        ans = min(ans, t)
        return
    njd = [row[:] for row in jd]

    ax,ay = arr[0]
    a = jd[ax][ay]
    for di in CC[a]:
        gogo(ax,ay,di,jd)
        dfs(arr[1:], jd)
        jd = [row[:] for row in njd]


dfs(p, jido)
print(ans)
