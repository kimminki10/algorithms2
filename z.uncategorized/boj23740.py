from collections import deque
import sys
input = sys.stdin.readline


K = int(input())
sec = [list(map(int, input().split())) for _ in range(K)]
sec.sort()
sec = deque(sec)

res = []
while sec:
    if len(sec) == 1:
        res += sec
        break
    bl, br, bc = sec.popleft()
    cl, cr, cc = sec.popleft()

    if cl <= br:
        sec.appendleft([bl, max(br, cr), min(bc, cc)])
    if br < cl:
        res.append([bl, br, bc])
        sec.appendleft([cl, cr, cc])


print(len(res))
for row in res:
    print(*row)
