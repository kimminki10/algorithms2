from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    heappush(nums, int(input()))
for _ in range(N):
    print(heappop(nums))