import sys
input = sys.stdin.readline

INF = 987654321
V, E = map(int, input().split())
jido = []
for i in range(V):
    line = [ INF ] * V
    jido.append(line)

for _ in range(E):
    a, b, c = map(int, input().split())
    jido[a-1][b-1] = min(jido[a-1][b-1], c)


for k in range(V):
    for i in range(V):
        for j in range(V):
            jido[i][j] = min(jido[i][j], jido[i][k] + jido[k][j])

result = INF
for i in range(V):
    result = min(result, jido[i][i])

if result == INF:
    print(-1)
else:
    print(result)