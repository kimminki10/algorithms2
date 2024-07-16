from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M = len(str(N))

comb = list(combinations(range(M), 2))

def gogo(N, M, K):
    result = -1
    q = [(N, K)]
    visit = set()
    visit.add((N, K))

    while q:
        c, d = q.pop(0)

        if d == 0:
            if result < c:
                result = c
            continue

        c = list(str(c))
        for a, b in comb:
            if a == 0 and c[b] == '0': continue
            c[a], c[b] = c[b], c[a]
            cc = int("".join(c))
            if (cc, d-1) not in visit:
                q.append((cc, d-1))
                visit.add((cc, d-1))
            c[a], c[b] = c[b], c[a]
    
    return result


print(gogo(N, M, K))