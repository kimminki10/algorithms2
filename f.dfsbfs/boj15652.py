import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def combination(l, r):

    def dfs(n, m, ans):
        if m == 0:
            print(' '.join([str(i) for i in ans]))
            return
        
        if ans:
            small = ans[-1]
        else:
            small = 1

        for next in range(small, n+1):
            ans.append(next)
            dfs(n, m-1, ans)
            ans.pop()
    dfs(len(l), r, [])

combination(range(N), M)