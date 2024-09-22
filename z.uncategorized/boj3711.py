from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())

def testcase():
    G = int(input())
    arr = [int(input()) for _ in range(G)]
    m = 1
    while True:
        d = defaultdict(lambda:0)
        for v in arr:
            idx = v % m
            if d[idx] != 0:
                break
            d[idx] = 1
        else:
            break
        m += 1
    print(m)

for _ in range(N):
    testcase()