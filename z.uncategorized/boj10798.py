import sys
input = sys.stdin.readline

jido = [list(input().rstrip()) for _ in range(5)]
m = [['' for _ in range(15)] for _ in range(5)]
for i in range(5):
    for j in range(len(jido[i])):
        m[i][j] = jido[i][j]

ans = ''
for j in range(15):
    for i in range(5):
        ans += m[i][j]
print(ans)