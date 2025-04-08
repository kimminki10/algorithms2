import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
opl = []
for i, v in enumerate(op):
    opl += list('+-*/')[i] * v
visit = [0] * len(opl)
maxv = float('-inf')
minv = float('inf')

def dfs(idx, val):
    global maxv, minv
    if idx == N-1:
        maxv = max(maxv, val)
        minv = min(minv, val)
        return
    for i,v in enumerate(opl):
        if visit[i] == 1: continue
        visit[i] = 1
        match v:
            case '+': dfs(idx+1, val+A[idx+1])
            case '-': dfs(idx+1, val-A[idx+1])
            case '*': dfs(idx+1, val*A[idx+1])
            case '/':
                if val < 0:
                    dfs(idx+1, -(-val // A[idx+1]))
                else:
                    dfs(idx+1, val // A[idx+1])
        visit[i] = 0
dfs(0, A[0])
print(maxv)
print(minv)