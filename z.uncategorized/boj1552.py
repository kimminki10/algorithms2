from collections import deque
from functools import reduce
from itertools import permutations
import sys
input = sys.stdin.readline


N = int(input())
jido = []
for _ in range(N):
    row = []
    for v in input().strip():
        if '0' <= v <= '9':
            row.append(ord(v) - ord('0'))
        else:
            row.append((ord(v) - ord('A') + 1) * -1)
    jido.append(row)


def color(i, num, visit, selected):
    q = deque([i])
    visit[i] = num

    while q:
        cur = q.popleft()
        for a,b in selected:
            if visit[b] == -1 and a == cur:
                visit[b] = num
                q.append(b)

def count_cycle(selected, N) -> int:
    visit = [-1] * N
    res = 0
    for i in range(N):
        if visit[i] == -1:
            color(i, res, visit, selected)
            res += 1
    return res

maxa = -987654321
mina = 987654321
for perm in permutations(range(N), N):
    selected = [[i,v] for i, v in enumerate(perm) ]
    count = count_cycle(selected, N)
    mm = reduce(lambda x,y: x*y, [jido[a][b] for a, b in selected])
    if count % 2 == 0: mm *= -1
    maxa = max(maxa, mm)
    mina = min(mina, mm)
print(mina)
print(maxa)