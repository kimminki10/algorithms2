import sys
input = sys.stdin.readline

jido = [ list(map(int, list(input().strip()))) for _ in range(9) ]

rows = [[ 0 ] * 10 for _ in range(9)]
cols = [[ 0 ] * 10 for _ in range(9)]
square = [[0] * 10 for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if jido[i][j] == 0:
            zeros.append((i,j))
        else:
            v = jido[i][j]
            rows[i][v] = 1
            cols[j][v] = 1
            sx = (i // 3) * 3
            sy = (j // 3)
            square[sx+sy][v] = 1

zeroslen = len(zeros)

def check_row(x, v):
    return rows[x][v] == 0

def check_col(y, v):
    return cols[y][v] == 0

def check_square(x, y, v):
    sx = (x // 3) * 3
    sy = (y // 3)
    return square[sx+sy][v] == 0

def is_possible(x, y, v):
    if check_col(y, v) and\
       check_row(x, v) and\
        check_square(x, y, v):
        return True
    return False


def dfs(cur):
    if cur == zeroslen:
        for r in jido:
            print(''.join([str(i) for i in r]))
        sys.exit(0)

    x = zeros[cur][0]
    y = zeros[cur][1]

    if jido[x][y] == 0:
        for i in range(1, 10):
            if is_possible(x, y, i):
                jido[x][y] = i
                rows[x][i] = 1
                cols[y][i] = 1
                square[(x//3)*3+y//3][i] = 1
                dfs(cur+1)
                rows[x][i] = 0
                cols[y][i] = 0
                square[(x//3)*3+y//3][i] = 0
                jido[x][y] = 0
    else:
        dfs(cur+1)

dfs(0)