import sys
input = sys.stdin.readline

def is_possible(m, p, srr):
    if srr[0] == 1 and srr[m] + p >= m:
        return True
    for i in range(1000001-m):
        if srr[i+m] - srr[i] + p >= m:
            return True
    return False

def solve():
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    srr = [ 0 for _ in range(1000001) ]
    for a in arr:
        srr[a] = 1
    for i in range(1, 1000001):
        srr[i] += srr[i-1]

    l = 0
    r = n+p
    while l <= r:
        m = (l+r) // 2
        if is_possible(m, p, srr):
            ans = m
            l = m + 1
        else: r = m - 1
    return ans

def testcase(tc):
    result = solve()
    print(f"#{tc} {result}")


T = int(input())
for i in range(T):
    testcase(i+1)