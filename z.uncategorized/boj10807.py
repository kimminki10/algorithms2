from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = map(int, input().split())
v = int(input().strip())
d = defaultdict(lambda:0)

for i in arr:
    d[i] += 1

print(0 if v not in d else d[v])