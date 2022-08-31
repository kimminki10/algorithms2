import sys
input = sys.stdin.readline

N = int(input())
narr = set(list(map(int, input().split())))

M = int(input())
marr = list(map(int, input().split()))

result = []
for m in marr:
    if m in narr:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))