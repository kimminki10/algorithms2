import sys
input = sys.stdin.readline

S = input().strip()
N = len(S)
d = [[0] * N for _ in range(N)]

for j in range(1,N):
    for l in range(N-j):
        r = l+j
        if (S[l]=='a' and S[r]=='t') or (S[l]=='g' and S[r]=='c'):
            d[l][r] = d[l+1][r-1] + 2
        for k in range(l, r):
            if d[l][r] < d[l][k]+d[k+1][r]:
                d[l][r]=d[l][k]+d[k+1][r]
print(d[0][-1])