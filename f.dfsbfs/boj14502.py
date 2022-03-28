from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

zero_count = 0
virus = []
jido = []
for x in range(N):
    l = []
    for y, i in enumerate(input().split()):
        i = int(i)
        l.append(i)

        if i == 2:
            virus.append([x,y])
        elif i == 0:
            zero_count += 1
    jido.append(l)

def is_all_zero(p):
    for (x,y) in p:
        if jido[x][y] != 0:
            return False
    return True

def is_valid_zero(x,y):
    if not (0<= x < N and 0 <= y < M): return False
    if jido[x][y] == 0: return True
    return False

direct = [[0,1],[1,0],[-1,0],[0,-1]]
def count_safe_zone():
    visit = [[0] * M for _ in range(N)]
    contaminate_count = 0
    for (x,y) in virus:
        q = [(x,y)]

        while q:
            cx,cy = q.pop(0)

            for [dx,dy] in direct:
                nx = cx+dx
                ny = cy+dy
                if is_valid_zero(nx,ny) and visit[nx][ny] == 0:
                    contaminate_count += 1
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    return zero_count - contaminate_count - 3


answer = 0
for cc in combinations(range(N*M), 3):
    p = list(map(lambda v: (v//M, v%M), cc))
    
    if is_all_zero(p):
        for (x,y) in p:
            jido[x][y] = 1

        answer = max(answer, count_safe_zone())
        
        for (x,y) in p:
            jido[x][y] = 0

print(answer)