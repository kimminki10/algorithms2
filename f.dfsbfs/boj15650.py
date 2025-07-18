import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(cur, d, ans):
    if d == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(cur+1, N+1):
        dfs(i,d+1, ans+[i])

dfs(0,0, [])