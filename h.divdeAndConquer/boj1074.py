import sys
input = sys.stdin.readline

N, r, c = list(map(int, input().split()))
result = 0

def go(n, sx, sy, count):
    global result

    m = n//2

    if n == 2:
        if sx     == r and sy     == c: result = count
        if sx     == r and (sy+1) == c: result = count + 1
        if (sx+1) == r and sy     == c: result = count + 2
        if (sx+1) == r and (sy+1) == c: result = count + 3
        return

    sxm = sx+m
    sym = sy+m
    sxn = sx+n
    syn = sy+n
    if sx <= r < sxm and sy <= c < sym:
        go(m, sx, sy, count)
    if sx <= r < sxm and sym <= c < syn:
        go(m, sx, sym, count+m*m)
    if sxm <= r < sxn and sy <= c < sym:
        go(m, sxm, sy, count+m*m*2)
    if sxm <= r < sxn and sym <= c < syn:
        go(m, sxm, sym, count+m*m*3)

go(2**N, 0, 0, 0)
print(result)