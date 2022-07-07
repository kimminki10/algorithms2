import sys
input = sys.stdin.readline

n = int(input().rstrip())

cache = [0] * 1001

cache[1] = 1
cache[2] = 2

for i in range(3, n+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 10007

print(cache[n])
