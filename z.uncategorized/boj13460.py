import sys
input = sys.stdin.readline

# 2 sec
N, M = map(int, input().split()) # 3 <= N, M <= 10
jido = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if jido[i][j] == 'R':
            red = (i, j)
            jido[i][j] = '.'
        elif jido[i][j] == 'B':
            blue = (i, j)
            jido[i][j] = '.'


def lift(jido, red, blue, dx, dy):
    rx, ry = red
    ans = 1
    for _ in range(2):
        while True:
            if jido[rx + dx][ry + dy] == '#' or (rx + dx, ry + dy) == blue:
                break
            if jido[rx + dx][ry + dy] == 'O':
                rx, ry = -1, -1
                ans = 0
                break
            rx += dx
            ry += dy
        red = (rx, ry)
        bx, by = blue
        while True:
            if jido[bx + dx][by + dy] == '#' or (bx + dx, by + dy) == red:
                break
            if jido[bx + dx][by + dy] == 'O':
                return -1, red, (bx + dx, by + dy)
            bx += dx
            by += dy
        blue = (bx, by)
    return ans, (rx, ry), (bx, by)


def bfs(jido, red, blue):
    q = [(red, blue, 0)]
    visited = set()
    visited.add((red, blue))
    while q:
        red, blue, cnt = q.pop(0)
        if cnt >= 10:
            return -1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            result, new_red, new_blue = lift(jido, red, blue, dx, dy)
            if result == -1:
                continue
            elif result == 0:
                return cnt + 1
            if (new_red, new_blue) not in visited:
                visited.add((new_red, new_blue))
                q.append((new_red, new_blue, cnt + 1))
    return -1

#print(lift(jido, red, blue, 0, 1))
result = bfs(jido, red, blue)
print(result)