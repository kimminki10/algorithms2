import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 ** 14)

N = int(input().rstrip())
T = []
P = []
for _ in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)


result = 0
def dfs(idx, profit):
    if idx > N: return
    global result
    result = max(profit, result)
    if idx >= N: return

    # choose
    dfs(idx+T[idx], profit+P[idx])
    # not choose
    dfs(idx+1, profit)


dfs(0, 0)
print(result)