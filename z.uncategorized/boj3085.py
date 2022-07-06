import sys
input = sys.stdin.readline

N = int(input().rstrip())
jido = [list(input().rstrip()) for _ in range(N)]


def count_same(x, y, jido, d, N):
    """d: direction horizontal on 1 vertical on 0"""

    count = 1
    v = jido[x][y]
    if d == 0:
        for i in range(x+1, N):
            if jido[i][y] == v:
                count += 1
            else: break
        for i in range(x-1, -1, -1):
            if jido[i][y] == v:
                count += 1
            else: break
    else:
        for j in range(y+1, N):
            if jido[x][j] == v:
                count += 1
            else: break
        for j in range(y-1, -1, -1):
            if jido[x][j] == v:
                count += 1
            else: break
    return count


def solve(N, jido):
    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, count_same(i, j, jido, 0, N))
            result = max(result, count_same(i, j, jido, 1, N))
            if j+1 < N and jido[i][j] != jido[i][j+1]:
                jido[i][j], jido[i][j+1] = jido[i][j+1], jido[i][j]
                result = max(result, count_same(i, j  , jido, 1, N))
                result = max(result, count_same(i, j  , jido, 0, N))
                result = max(result, count_same(i, j+1, jido, 0, N))
                jido[i][j], jido[i][j+1] = jido[i][j+1], jido[i][j]
            
            if i+1 < N and jido[i][j] != jido[i+1][j]:
                jido[i][j], jido[i+1][j] = jido[i+1][j], jido[i][j]
                result = max(result, count_same(i  , j, jido, 0, N))
                result = max(result, count_same(i  , j, jido, 1, N))
                result = max(result, count_same(i+1, j, jido, 1, N))
                jido[i][j], jido[i+1][j] = jido[i+1][j], jido[i][j]
            
    return result


print(solve(N, jido))