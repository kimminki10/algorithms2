import sys
input = sys.stdin.readline

c = list(range(10))

def gogo(d, st, en=-1) -> list:
    if d == 0:
        return ['']

    result = []
    for i in range(st, en, -1):
        result += [ int(f"{i}{j}") for j in gogo(d-1, i-1) ]
    return result

for i in range(2,11):
    c += gogo(i, 9, 0)

c.sort()
num = int(input().strip())

print(-1 if num >= len(c) else c[num])