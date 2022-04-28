import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

jido = [[9876543210] * n for _ in range(n)]
citys = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    if jido[a-1][b-1] > c:
        jido[a-1][b-1] = min(jido[a-1][b-1], c)
        citys[a-1][b-1] = [a, b]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if jido[i][j] > jido[i][k] + jido[k][j]:
                jido[i][j] = jido[i][k] + jido[k][j]
                citys[i][j] = citys[i][k] + citys[k][j][1:]

for i in range(n):
    for j in range(n):
        if jido[i][j] == 9876543210:
            jido[i][j] = 0

for row in jido:
    print(' '.join([str(i) for i in row]))

for i in range(n):
    for j in range(n):
        if jido[i][j] == 0:
            print(0)
        else:
            print(len(citys[i][j]), ' '.join([str(v) for v in  citys[i][j]]))
