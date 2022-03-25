import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

direct = [[0,1],[1,0],[-1,0],[0,-1]]
def isPos(x, y):
    return 0<=x<N and 0<=y<M

def bfs(x, y):
    global paper
    visit = {}
    visit[(x, y)] = 1
    cheese_with_air = {}
    remove_list = []
    q = [(x, y)]

    while q:
        x, y = q.pop(0)

        for [i, j] in direct:
            a, b = x+i, y+j
            if isPos(a, b):
                if (a,b) not in visit:
                    visit[(a,b)] = 1
                    if paper[a][b] == 0:
                        q.append((a,b))
                    else:
                        cheese_with_air[(a,b)] = 1
                elif paper[a][b] == 1:
                    cheese_with_air[(a,b)] += 1
                    remove_list.append((a,b))
    
    result = len(remove_list)
    for (a,b) in remove_list:
        paper[a][b] = 0
    return result

count = 0
while True:
    re = bfs(0, 0)
    if re == 0: break
    count += 1
print(count)