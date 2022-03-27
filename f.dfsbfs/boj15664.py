import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))


def dfs(n, m, ans=[], visit=[0]*N):
    if m == 0:
        print(' '.join([str(arr[i]) for i in ans]))
        return

    if ans:
        small = ans[-1] + 1
    else:
        small = 0

    tmp = -1
    for next in range(small, n):
        if visit[next] == 1: continue
        if tmp == arr[next]: continue
        tmp = arr[next]

        visit[next] = 1
        ans.append(next)
        dfs(n, m-1, ans)
        ans.pop()
        visit[next] = 0

dfs(N, M, [])
