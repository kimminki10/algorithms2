from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
jido = [ list(map(int, input().split())) for _ in range(N) ]

def transpose(jido):
    return [ list(row) for row in zip(*jido) ]

def flip(jido):
    return [ row[::-1] for row in jido ]

def left(jido):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        y = 0
        for j in range(N):
            if jido[i][j] == 0:
                continue
            res[i][y] = jido[i][j]
            y += 1
        for j in range(1, N):
            if res[i][j] == 0:
                continue
            if res[i][j] == res[i][j-1]:
                res[i][j-1] *= 2
                res[i].pop(j)
                res[i].append(0)
    return res

def right(jido):
    return flip(left(flip(jido)))

def up(jido):
    return transpose(left(transpose(jido)))

def down(jido):
    return transpose(right(transpose(jido)))


def dfs(jido, depth):
    if depth == 5:
        return max(map(max, jido))
    
    res = 0
    res = max(res, dfs(left(jido), depth + 1))
    res = max(res, dfs(right(jido), depth + 1))
    res = max(res, dfs(up(jido), depth + 1))
    res = max(res, dfs(down(jido), depth + 1))
    return res

print(dfs(jido, 0))