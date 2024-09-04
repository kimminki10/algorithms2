import copy
import sys
input = sys.stdin.readline

N = int(input().strip())
jido = [ list(map(int, input().split())) for _ in range(N)]

maxa = -987654321

def flip(jido):
    for row in jido:
        for i in range(N//2):
            row[i], row[N-i-1] = row[N-i-1], row[i]

def diagonal(jido):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[j][i] = jido[i][j]
    return res

def goleft(jido):
    for row in jido:
        i = j = 0
        while i < N:
            if row[j] == 0:
                row[j:] = row[j+1:]+[0]
            else: j += 1
            i += 1
        for i in range(N-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1:] = row[i+2:]+[0]

def goright(jido):
    flip(jido)
    goleft(jido)
    flip(jido)

def goup(jido):
    jido[:] = diagonal(jido)
    goleft(jido)
    jido[:] = diagonal(jido)

def godown(jido):
    jido[:] = diagonal(jido)
    goright(jido)
    jido[:] = diagonal(jido)

def gogo(selected, arr):
    global maxa
    for i in selected:
        if i == 0: goleft(arr)
        elif i == 1: goright(arr)
        elif i == 2: goup(arr)
        elif i == 3: godown(arr)
    
    for row in arr:
        for v in row:
            maxa = max(maxa, v)

def dfs(cur, selected, jido):
    if cur == 5:
        gogo(selected, copy.deepcopy(jido[:]))
        return
    
    for i in range(4):
        selected.append(i)
        dfs(cur+1, selected, jido)
        selected.pop()
    
dfs(0, [], jido)
print(maxa)