import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
points = [list(map(int,input().split())) for _ in range(M)]
jido = [[0] * N for _ in range(H)]
for [x,y] in points:
    jido[x-1][y-1] = 1
    jido[x-1][y] = -1

def sub_good(jd, line):
    y = line
    for x in range(H):
        if jd[x][y] != 0:
            y += jd[x][y]
    return y == line


def is_good(jd):
    for y in range(N-1):
        if not sub_good(jd, y):
            return False
    return True


ans = float('inf')
def dfs(cur, depth, jd):
    global ans
    if is_good(jd):
        ans = min(ans, depth)
        return
    if depth == 3: return

    for n in range(cur, N*H):
        i,j = n//N, n%N
        if j == N-1 or jido[i][j] != 0 or jido[i][j+1] != 0:
            continue
        jd[i][j] = 1
        jd[i][j+1] = -1
        dfs(n+1, depth+1, jd)
        jd[i][j] = 0
        jd[i][j+1] = 0


dfs(0,0,jido)
if ans == float('inf'):
    ans = -1
print(ans)
