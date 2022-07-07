import sys
input = sys.stdin.readline

N = int(input().rstrip())

cache = [0] * (10**6 + 1)
for i in range(2, N+1):
    cache[i] = cache[i-1] + 1
    if i % 2 == 0 and cache[i] > cache[i // 2] + 1:
        cache[i] = cache[i // 2] + 1
    if i % 3 == 0 and cache[i] > cache[i // 3] + 1:
        cache[i] = cache[i // 3] + 1
print(cache[N])