import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(sorted(map(int, input().split())))


def dfs(n, m, ans=[]):
    if m == 0:
        print(' '.join([str(arr[i]) for i in ans]))
        return

    if ans:
        small = ans[-1]
    else:
        small = 0

    for next in range(small, n):
        ans.append(next)
        dfs(n,m-1,ans)
        ans.pop()

dfs(N, M)