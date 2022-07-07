import sys
input = sys.stdin.readline

n = int(input())

cache = [ 0 ] * 1001
cache[1] = 1
cache[2] = 3

for i in range(3, n+1):
    cache[i] += cache[i-1]
    cache[i] += cache[i-2] * 2
    cache[i] %= 10007
print(cache[n])