import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def combi(arr, m):

    def dfs(n, m, ans):
        if m == 0:
            print(' '.join([str(arr[i-1]) for i in ans]))
            return
        
        if ans:
            small = ans[-1] + 1
        else:
            small = 1

        for next in range(small, n+1):
            ans.append(next)
            dfs(n, m-1, ans)
            ans.pop()
    dfs(len(arr), m, [])

combi(arr, M)