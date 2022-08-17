import sys
input = sys.stdin.readline

def testcase():
    a, b = map(int, input().split())
    r = a
    for _ in range(1, b):
        r = r * a % 10
    r %= 10
    if r == 0:
        r = 10
    print(r)


for _ in range(int(input().rstrip())):
    testcase()
