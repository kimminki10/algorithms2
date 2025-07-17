from math import gcd
import sys
input = sys.stdin.readline


N = int(input())
positions = [int(input()) for _ in range(N)]

p_diff = [ b-a for a,b in zip(positions[:-1], positions[1:]) ]
space = gcd(*p_diff)

print((positions[-1] - positions[0]) // space + 1 - N)
