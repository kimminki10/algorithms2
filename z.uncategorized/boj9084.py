import sys
input = sys.stdin.readline

T = int(input())

def testcase():
    N = int(input())
    C = list(map(int,input().split()))
    M = int(input())

    d = [0] * (M+1)
    d[0] = 1
    for c in C:
        for m in range(c, M+1):
            d[m] += d[m-c]
    print(d[M])

for _ in range(T):
    testcase()

