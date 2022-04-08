import sys
input = sys.stdin.readline


def eratos(n):
    n = n+1
    sieve = [ True ] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

N = int(input())
pnum = eratos(N)
plen = len(pnum)

if plen == 0:
    print(0)
    sys.exit(0)

result = 0
i = 0; j = 1
ss = pnum[0]
while j <= plen:
    if ss == N:
        result += 1

    if ss >= N:
        ss -= pnum[i]
        i += 1
    else:
        if j < plen: ss += pnum[j]
        j += 1
    
print(result)