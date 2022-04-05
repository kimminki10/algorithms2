from collections import defaultdict
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
half = N // 2
ans = 0

d = defaultdict(lambda: 0)
def left(idx, sum):
    if idx == half:
        d[sum] += 1
        return

    left(idx+1, sum)
    left(idx+1, sum + arr[idx])

def right(idx, sum):
    global ans
    if idx == N:
        ans += d[S-sum]
        return

    right(idx+1, sum)
    right(idx+1, sum+arr[idx])

left(0, 0)
right(half, 0)
if S == 0: 
    ans -= 1
print(ans)