from itertools import pairwise
import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

diff = [ (b-a, i) for i, (a, b) in enumerate(pairwise(arr))]
diff.sort(reverse=True)

idx = [ i for v, i in diff[:K-1] ] + [-1] + [N-1]
idx.sort()
cost = sum([ arr[b]-arr[a+1] for a, b in pairwise(idx)])
print(cost)