import sys
input = sys.stdin.readline


N = int(input())

def solve(N):
    if N == 1: return 1

    t = 1
    a = 1
    while t <= (N / 10): 
        t *= 10
        a += 1


    result = 0
    while N > 0:
        result += (N - t+1) * a
        N -= N-t+1
        t //= 10
        a -= 1
    return result

print(solve(N))