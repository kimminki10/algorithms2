import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
print(sum([ (a-B +C-1) // C  for a in A if a > B]) + N)