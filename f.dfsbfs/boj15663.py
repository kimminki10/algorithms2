import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))

permu = set()
def dfs(n, m, ans=[], visit=[0]*N):
    if m == 0:
        item = ' '.join([str(arr[i]) for i in ans])
        print(item)
        return
    tmp = -1
    for next in range(n):
        if visit[next] == 1: continue
        if tmp == arr[next]: continue
        tmp = arr[next]

        visit[next] = 1
        ans.append(next)
        dfs(n,m-1,ans,visit)
        ans.pop()
        visit[next] = 0

dfs(N, M)
