import sys
input = sys.stdin.readline

N, L = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]

def transpose(jido):
    return [ list(row) for row in zip(*jido) ]

def is_good(arr):
    cur = arr[0]
    check = [False] * N
    i = 0
    while i < N:
        if arr[i] == cur:
            i += 1
            continue
        if cur - 1 == arr[i]:
            for j in range(i, i+L):
                if j >= N or arr[j] != cur-1 or check[j]:
                    return False
                check[j] = True
        elif cur + 1 == arr[i]:
            for j in range(i-1, i-L-1, -1):
                if j < 0 or arr[j] != cur or check[j]:
                    return False
                check[j] = True
        else:
            return False
        cur = arr[i]
        i += 1
    return True

def check(jido):
    res = 0
    for row in jido:
        if is_good(row):
            res += 1
    return res


ans = check(jido) + check(transpose(jido))
print(ans)