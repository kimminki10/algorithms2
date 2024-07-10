import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
C = {}
for _ in range(N):
    a, b = input().split()
    C[a] = int(b)

base = 0
for i in range(K):
    t = input().strip()
    base += C[t]
    del C[t]

ll = sorted(list(C.values()))
minv = base+sum(ll[:M-K])
maxv = base+sum(ll[-(M-K):]) if M > K else base
print(minv, maxv)