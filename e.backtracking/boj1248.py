import sys
input = sys.stdin.readline


def dfs(idx, mat, answer, subsum):
    if idx == len(mat):
        print(' '.join([str(r) for r in answer]))
        exit(0)

    st = -10
    en = 11
    for j in range(idx+1):
        if mat[j][idx] == '0':
            if -10 <= -(subsum[idx]-subsum[j]) <= 10:
                st = -(subsum[idx]-subsum[j])
                en = st+1
            else: return
        elif mat[j][idx] == '-':
            v = -(subsum[idx]-subsum[j])
            if v <= -10: return
            en = min(en, v)
        else:
            v = -(subsum[idx]-subsum[j]) + 1
            if v >= 11: return
            st = max(st, v)
    
    for i in range(st, en):
        dfs(idx+1, mat, answer+[i], subsum+[subsum[-1] + i])


def solve():
    n = int(input().rstrip())
    line = list(input().rstrip())
    
    mat = [ [-1] * n for _ in range(n) ]

    st = 0
    en = 0
    for i, row in enumerate(mat):
        st = en
        en = en + n - i
        row[i:] = line[st:en]

    dfs(0, mat, [], [0])


solve()