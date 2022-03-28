import sys
input = sys.stdin.readline

MOD =  1_000_000_007

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def mulmul(x, y, p):
    ans = 1
    while y > 0:
        if y % 2 != 0:
            ans *= x
            ans %= p
        
        x *= x
        x %= p
        y //= 2
    return ans

M = int(input())
ans = 0
for _ in range(M):
    N, S = map(int, input().split())

    g = gcd(N, S)
    N //= g
    S //= g

    bp = mulmul(N, MOD-2, MOD)
    ans += S*bp % MOD
    ans %= MOD

print(ans)
