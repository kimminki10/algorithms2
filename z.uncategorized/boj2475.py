import sys
input = sys.stdin.readline

arr = map(int, input().split())
result = sum(map(lambda x : x*x, arr)) % 10
print(result)