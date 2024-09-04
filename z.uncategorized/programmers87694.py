from collections import deque

LINE = 1
BLOCK = 2

def is_in_line(lines, cx,cy, nx,ny) -> bool:
    for a,b,x,y in lines:
        if a <= cx <= x and a <= nx <= x and\
           b <= cy <= y and b <= ny <= y:
            return True
    return False
    
def bfs(jido, lines, sx, sy, tx, ty) -> int:
    di = [[1,0],[0,1],[-1,0],[0,-1]]
    visit = set()
    q = deque()
    q.append((sx,sy, 0))
    visit.add((sx,sy))
    
    while q:
        cx, cy, d = q.popleft()
        
        for dx,dy in di:
            nx,ny = cx+dx,cy+dy
            if jido[nx][ny] == LINE and (nx,ny) not in visit and is_in_line(lines, cx, cy, nx,ny):
                visit.add((nx,ny))
                q.append((nx,ny,d+1))
                if nx == tx and ny == ty:
                    return d+1
    return -1
    

def fill(jido, a,b,x,y) -> None:
    for i in range(a, x+1):
        for j in range(b, y+1):
            if jido[i][j] == BLOCK: continue
            if i == a or i == x or j == b or j == y:
                jido[i][j] = LINE
            else:
                jido[i][j] = BLOCK
                

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    jido = [ [0] * 52 for _ in range(52) ]
    lines = []
    for a,b,x,y in rectangle:
        fill(jido, a,b,x,y)
        lines.extend([[a,b,x,b],[a,y,x,y], [a,b,a,y],[x,b,x,y]])
    
    answer = bfs(jido, lines, characterX, characterY, itemX, itemY)
    
    return answer

rectangle, characterX, characterY, itemX, itemY = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8
rectangle, characterX, characterY, itemX, itemY = [[2,2,5,5],[1,3,6,4],[3,1,4,6]],1, 4, 6, 3
print(solution(rectangle, characterX, characterY, itemX, itemY))