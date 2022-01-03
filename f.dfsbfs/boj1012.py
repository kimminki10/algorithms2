"""
유기농 배추
주의사항: dfs 는 RecursionError 가 났다. 최대 깊이가 1000이 넘으면 안되는 것 같다.
"""
import sys
input = sys.stdin.readline

def is_valid(x, y, M, N, d):
    if x < 0 or x >= M: return False
    if y < 0 or y >= N: return False
    if d[y][x] != -1: return False
    return True

def dfs(x, y, v, M, N, d):
    if not is_valid(x, y, M, N, d): return
    
    d[y][x] = v
    dfs(x-1, y, v, M, N, d)
    dfs(x+1, y, v, M, N, d)
    dfs(x, y-1, v, M, N, d)
    dfs(x, y+1, v, M, N, d)

def bfs(x, y, v, M, N, d):
    q = []
    q.append([x, y])

    while len(q) > 0:
        a, b = q.pop()
        if not is_valid(a, b, M, N, d): continue
        
        d[b][a] = v
        q.append([a-1, b])
        q.append([a+1, b])
        q.append([a, b-1])
        q.append([a, b+1])
        


def testcase():
    M, N, K = map(int, input().split())

    d = [ [ 0 for _ in range(M)] for _ in range(N) ]

    for _ in range(K):
        x, y = map(int, input().split())
        d[y][x] = -1

    bug_num = 0
    for j in range(N):
        for i in range(M):
            if d[j][i] == -1:
                bug_num += 1
                bfs(i, j, bug_num, M, N, d)
    
    print(bug_num)


T = int(input())
for _ in range(T):
    testcase()