import sys
input = sys.stdin.readline

n = int(input().strip())
print(sum([int(input().strip()) for _ in range(n)]))
