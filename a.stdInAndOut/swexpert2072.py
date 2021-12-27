
import sys
input = sys.stdin.readline


def solve(t):
    l = list(map(int, input().split()))
    s = 0
    for i in l:
        if i % 2 == 1:
            s += i
    
    print(f"#{t} {s}")


T = int(input())
for t in range(T):
    solve(t+1)