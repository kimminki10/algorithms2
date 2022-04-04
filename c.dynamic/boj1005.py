import sys
sys.setrecursionlimit(2**16)
input = sys.stdin.readline

T = int(input())

def get_minimum_time(w):
    if visit[w] != -1: return visit[w]
    if P[w] == []:
        visit[w] = D[w]
        return D[w]
    maxv = max([ get_minimum_time(item) for item in P[w]])
    visit[w] = maxv+D[w]
    return visit[w]

def testcase():
    global edges, P, D, visit
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    P = [[] for _ in range(N)]
    visit = [ -1 ] * N
    for _ in range(K):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        P[b-1].append(a-1)
    W = int(input())

    print(get_minimum_time(W-1))


for _ in range(T):
    testcase()
