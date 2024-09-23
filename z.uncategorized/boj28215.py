from itertools import combinations
from functools import reduce
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]

dist = lambda a,b: abs(a[0]-b[0])+abs(a[1]-b[1])

def daepiso_dist(v, comb):
    return reduce(min, map(lambda x: dist(v, x), comb))

ans = 987654321
for comb in combinations(arr, K):
    ans = min(ans, reduce(max, map(lambda x: daepiso_dist(x, comb), arr)))
print(ans)
        