import sys
input = sys.stdin.readline

def testcase():
    print(sum(map(int, input().split(','))))
def solve():
    t = int(input())
    for _ in range(t):
        testcase()
solve()
