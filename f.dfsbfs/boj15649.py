import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [0] * 10

def dfs(depth: int, arr: list):
    if depth == M:
        print(*arr)

    for i in range(1, N+1):
        if visit[i]: continue

        visit[i] = 1
        arr.append(i)
        dfs(depth+1, arr)
        arr.pop(-1)
        visit[i] = 0

dfs(0, [])