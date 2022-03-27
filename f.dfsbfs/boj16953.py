import sys
input = sys.stdin.readline

A, B = map(int, input().split())

answer = 987654321
def dfs(cur, depth):
    global answer
    if cur > B:
        return

    if cur == B:
        answer = min(answer, depth)
        return

    dfs(cur * 2, depth+1)
    dfs(cur * 10 + 1, depth+1)

dfs(A, 0)
if answer == 987654321:
    print(-1)
else:
    print(answer + 1)