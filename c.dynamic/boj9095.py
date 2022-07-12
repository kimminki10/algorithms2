import sys
input = sys.stdin.readline


def testcase():
    N = int(input().rstrip())
    d = [ 0 ] * 12

    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, 12):
        d[i] += d[i-1]
        d[i] += d[i-2]
        d[i] += d[i-3]
    print(d[N])
    

T = int(input().rstrip())
for i in range(T):
    testcase()