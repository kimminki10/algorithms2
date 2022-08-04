import sys
input = sys.stdin.readline


def min_time(road):
    result = 1000000001
    for r in road:
        if r:
            result = min(result, r[0][0])
    return result


def solve():
    N = int(input().rstrip())
    result = [-1] * N
    road = [[] for _ in range(4)]

    for i in range(N):
        t, w = input().split()
        road[ord(w) - ord('A')].append([int(t), i])

    mtime = 0
    idx = 0
    while idx < N:
        mtime = max(mtime, min_time(road))
        cur_go = []
        for i in range(4):
            lidx = (i-1) % 4
            if road[i] and road[i][0][0] <= mtime and ((not road[lidx]) or road[lidx][0][0] > mtime):
                cur_go.append(i)
        if not cur_go:
            break
        for i in cur_go:
            _, ri = road[i].pop(0)
            result[ri] = mtime
            idx += 1
        mtime += 1
        
    return result

res = solve()
for i in res:
    print(i)
