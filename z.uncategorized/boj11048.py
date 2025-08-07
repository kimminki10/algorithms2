import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
ans[0][0] = jido[0][0]
di = [[0,1],[1,0],[1,1]]
for i in range(N):
    for j in range(M):
        for dx,dy in di:
            nx,ny = i+dx, j+dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            ans[nx][ny] = max(ans[nx][ny], ans[i][j]+jido[nx][ny])

print(ans[N-1][M-1])