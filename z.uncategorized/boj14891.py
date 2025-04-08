import sys
input = sys.stdin.readline

A = [ list(map(int, input().rstrip())) for _ in range(4) ]
K = int(input())

def rotate(n: int, d: int, visit: set):
    if n in visit: return
    visit.add(n)
    if n == 0 and A[0][2] != A[1][6]:
        rotate(1, -d, visit)
    elif n == 1:
        if A[0][2] != A[1][6]:
            rotate(0, -d, visit)
        if A[1][2] != A[2][6]:
            rotate(2, -d, visit)
    elif n == 2:
        if A[1][2] != A[2][6]:
            rotate(1, -d, visit)
        if A[2][2] != A[3][6]:
            rotate(3, -d, visit)
    elif n == 3:
        if A[2][2] != A[3][6]:
            rotate(2, -d, visit)
    
    if d == 1:
        A[n] = [A[n][-1]] + A[n][:-1]
    else:
        A[n] = A[n][1:] + [A[n][0]]
    
    
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1

    rotate(n, d, set())

ans = 0
for i in range(4):
    ans += A[i][0] * (2 ** i)
print(ans)