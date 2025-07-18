import sys
input = sys.stdin.readline


def gogo(h):
    n = len(h)
    if len(h) <= 1:
        if h: return h[0]
        else: return 0
    elif len(h) <= 2:
        return max(min(h) * 2, max(h))

    m = n//2
    l = gogo(h[:m])
    r = gogo(h[m+1:])

    c = h[m]
    li = m-1
    ri = m+1
    curh = h[m]
    while 0 <= li and ri < n:
        if h[li] < h[ri]:
            if h[ri] < curh:
                curh = h[ri]
            c = max(c, curh * (ri-li))
            ri += 1
        else:
            if h[li] < curh:
                curh = h[li]
            c = max(c, curh * (ri-li))
            li -= 1

    while 0 <= li:
        if h[li] < curh:
            curh = h[li]
        c = max(c, curh * (ri-li))
        li -= 1
    while ri < n:
        if h[ri] < curh:
            curh = h[ri]
        c = max(c, curh * (ri-li))
        ri += 1

    return max(l,r,c)


while True:
    line = list(map(int, input().split()))
    if line == [0]: break
    _, *h = line
    print(gogo(h))