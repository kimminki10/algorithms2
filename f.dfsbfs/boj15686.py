from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

jido = [[int(i) for i in input().split()] for _ in range(N)]

chickens = []
jip = []
for x in range(N):
    for y in range(N):
        if jido[x][y] == 2:
            chickens.append((x,y))
        if jido[x][y] == 1:
            jip.append((x,y))

def dist(x, y, a, b):
    return abs(x-a) + abs(y-b)

answer = 987654321
for c in combinations(chickens, M):
        sub_sum = sum([min([dist(i[0],i[1],j[0],j[1]) for i in c]) for j in jip])
        answer = min(sub_sum, answer)
print(answer)