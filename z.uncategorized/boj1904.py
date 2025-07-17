import sys
input = sys.stdin.readline

N = int(input())
a,b = 0,1
for i in range(N):
    a,b = b,(a+b)%15746

print(b % 15746)