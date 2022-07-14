import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

arr.sort()

p = 0
for i in range(N):
    if p + 1 < arr[i]: break
    p += arr[i]

print(p+1)