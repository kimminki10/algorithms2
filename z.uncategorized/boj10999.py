import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nrr = [0]+[int(input()) for _ in range(N)]

tree = [0] * (N * 4)
lazy = [0] * (N * 4)

def build(s, e, i):
    if s == e:
        tree[i] = nrr[s]
        lazy[i] = 0
        return
    m = (s + e) // 2
    build(s, m, i*2)
    build(m+1, e, i*2+1)
    tree[i] = tree[i*2] + tree[i*2+1]
    lazy[i] = 0

def update_range(s, e, i, l, r, v):
    push(s, e, i)
    if e < l or r < s: return
    if l <= s and e <= r:
        tree[i] += (e-s+1) * v
        if s != e:
            lazy[i*2] += v
            lazy[i*2+1] += v
        return

    m = (s + e) // 2
    update_range(s, m, i*2, l, r, v)
    update_range(m+1, e, i*2+1, l, r, v)
    tree[i] = tree[i*2] + tree[i*2+1]


def push(s, e, i):
    if lazy[i] != 0:
        tree[i] += (e-s+1) * lazy[i]
        if s != e:
            lazy[i*2] += lazy[i]
            lazy[i*2+1] += lazy[i]
        lazy[i] = 0

def query(s, e, i, l, r):
    push(s, e, i)
    if e < l or r < s: return 0
    if l <= s and e <= r: return tree[i]

    m = (s + e) // 2
    return query(s, m, i*2, l, r) + query(m+1, e, i*2+1, l, r)


build(1, N, 1)

for _ in range(M+K):
    line = list(map(int, input().split()))
    if line[0] == 1:
        b,c,d = line[1:]
        update_range(1, N, 1, b, c, d)
    elif line[0] == 2:
        b,c = line[1:]
        print(query(1, N, 1, b, c))
        