from itertools import permutations
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

for item in permutations(arr, M):
    print(' '.join([ str(i) for i in item]))