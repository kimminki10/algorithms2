import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = [0] * N
sa = list(sorted(A))

for i, v in enumerate(A):
    idx = sa.index(v)
    sa[idx] = -1
    B[i] = idx

print(" ".join([str(i) for i in B]))