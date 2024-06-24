import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visit = [0] * N

def dfs(c, l):
    if len(l) == M:
        print(' '.join([str(arr[i]) for i in l]))
        return

    for i in range(c, N):
        if visit[i]: continue
        visit[i] = 1
        dfs(i, l[:]+[i])
        visit[i] = 0

dfs(0, [])