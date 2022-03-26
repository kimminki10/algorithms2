import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = range(1, N+1)

def combination(l, r):
    def dfs(n, r, ans):
        if r == 0:
            print(' '.join([str(i) for i in ans]))
            return
        
        if ans:
            small = ans[-1]+1
        else:
            small = 1

        for next in range(small, n+1):
            ans.append(next)
            dfs(n, r-1, ans)
            ans.pop()
    n = len(l)
    dfs(n, r, [])
combination(arr, M)