from collections import Counter
import math
import sys
input = sys.stdin.readline

N = int(input())

arr = [ int(input()) for _ in range(N)]
sarr = sorted(arr)
larr = len(arr)
cdict = Counter(sarr)

ss = sum(arr)

common = cdict.most_common(2)
commonv = max(common[-1], common[0], key=lambda x:x[1])[0]

print(math.floor(ss/N + 0.5))
print(sarr[larr//2])
print(commonv)
print(sarr[-1]-sarr[0])