import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def bfs(m, ans):
    if m == 0:
        print(' '.join([str(i) for i in ans]))
        return

    for i in range(N):
        ans.append(arr[i])
        bfs(m-1, ans)
        ans.pop()

bfs(M, [])
