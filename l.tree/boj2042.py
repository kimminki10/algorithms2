import sys
input = sys.stdin.readline

TN = 1
tree = [ 0 ] * 4000000

def change_val(idx, v):
    global tree

    idx = (TN+idx-1)
    tree[idx] = v

    idx >>= 1
    while idx > 0:
        tree[idx] = tree[idx*2] + tree[idx*2+1]
        idx >>= 1

def range_sum(ql, qr, idx=1, l=1, r=TN):
    if ql <= l and r <= qr: return tree[idx]
    if r < ql or qr < l:    return 0

    return range_sum(ql, qr, idx*2, l, (l+r)//2)\
        +  range_sum(ql, qr, idx*2+1, (l+r)//2+1, r)

N, M, K = map(int, input().split())

while TN < N: TN <<= 1
for i in range(N):
    tree[TN+i] = int(input())

for i in range(TN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2+1]

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        change_val(b, c)
    else:
        print(range_sum(b, c, 1, 1, TN))