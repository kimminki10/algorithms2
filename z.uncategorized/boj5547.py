from collections import defaultdict, deque
import sys
input = sys.stdin.readline


W, H = map(int, input().split())
jido = [ [0] * (W+2) for _ in range(H+2) ]
for i in range(H):
    row = list(map(int, input().split())) + [0]
    jido[i+1][1:] = row
di = [
    [[0,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]],
    [[0,1],[1,1],[1,0],[0,-1],[-1,0],[-1,1]],
]

def bfs(start):
    res = 0
    q = deque([start])
    visit = defaultdict(lambda:0)
    visit[start] = 1

    while q:
        a,b = q.popleft()

        for i,j in di[a%2]:
            x,y = a+i,b+j
            if visit[(x,y)] == 1: continue
            if 0 <= x <= H+1 and 0 <= y <= W+1:
                if jido[x][y] == 1:
                    res += 1
                    continue
                visit[(x,y)] = 1
                q.append((x,y))
    return res

print(bfs((0,0)))
