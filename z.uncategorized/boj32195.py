from bisect import bisect_right
import sys
input = sys.stdin.readline

N = int(input()) # 1 ~ 300000
arr = list(list(map(int, input().split())) for _ in range(N)) # -10^9 ~ 10^9
Q = int(input()) # 1 ~ 300000
R = [int(input()) for _ in range(Q)] # 1 ~ 10^9

ans = [0,0,0]
FOUL = 0
INSIDE = 1
HOMERUN = 2

def evaluate(x, y, r):
    d = x ** 2 + y ** 2
    if y >= x and y >= -x:
        if d <= r ** 2:
            return INSIDE
        else:
            return HOMERUN
    else:
        return FOUL

no_foul = [a for a in arr if evaluate(*a, 0) != FOUL]
ans[FOUL] = len(arr) - len(no_foul)
no_foul.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
square = [a[0] ** 2 + a[1] ** 2 for a in no_foul]
for r in R:
    idx = bisect_right(square, r ** 2)
    ans[INSIDE] = idx
    ans[HOMERUN] = len(no_foul) - idx
    print(*ans)