from collections import defaultdict
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [ list(map(int,input().split())) for _ in range(R) ]

CM = C-1
RM = R-1

aircleaner = []
for r in range(R):
    if room[r][0] == -1:
        aircleaner.append(r)

def is_possible(x, y):
    if not (0 <= x < R and 0 <= y < C): return False
    if room[x][y] == -1: return False
    return True

direct = [[1,0],[0,1],[-1,0],[0,-1]]
def spread():
    global room

    change = defaultdict(lambda: 0)
    for dx in range(R):
        for dy in range(C):
            if room[dx][dy] != 0 and room[dx][dy] >= 5:
                zz = room[dx][dy] // 5
                for [a, b] in direct:
                    nx = dx+a
                    ny = dy+b
                    if is_possible(nx, ny):
                        change[(dx,dy)] -= zz
                        change[(nx,ny)] += zz
            
    for k in change:
        room[k[0]][k[1]] += change[k]

def airflow():
    global room
    airx = aircleaner[0]
    room[airx-1][0] = 0
    for x in range(airx, 0, -1):
        room[x][0] = room[x-1][0]
    for y in range(CM):
        room[0][y] = room[0][y+1]
    for x in range(airx):
        room[x][CM] = room[x+1][CM]
    for y in range(CM, 0, -1):
        room[airx][y] = room[airx][y-1]
    room[airx][0] = -1

    airx += 1
    room[airx+1][0] = 0
    for x in range(airx, RM):
        room[x][0] = room[x+1][0]
    for y in range(CM):
        room[RM][y] = room[RM][y+1]
    for x in range(RM, airx, -1):
        room[x][CM] = room[x-1][CM]
    for y in range(CM, 0, -1):
        room[airx][y] = room[airx][y-1]
    room[airx][0] = -1

def timeflow():
    spread()
    airflow()

for _ in range(T):
    timeflow()

for x in aircleaner:
    room[x][0] = 0

answer = 0
for r in range(R):
    for c in range(C):
        if room[r][c] != 0:
            answer += room[r][c]
print(answer)