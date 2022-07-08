from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]


direct = [(-1,0), (0,-1)]
def is_all_good(x, y, visit):
    for (a,b) in direct:
        if visit[(x+a, y+b)] == 1:
            return False
    return True


result = -9876543210
def bfs(cur, visit, k, s):
    x = cur // M
    y = cur % M

    global result
    if k == 0:
        result = max(s, result)
        return
    if x >= N: return

    if is_all_good(x, y, visit):
        visit[(x, y)] = 1
        bfs(cur + 1, visit, k-1, s+jido[x][y])
        del visit[(x, y)]

    bfs(cur + 1, visit, k, s)

bfs(0, defaultdict(lambda: 0), K, 0)
print(result)
