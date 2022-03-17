import sys
input = sys.stdin.readline

INF = 987654321
def bellford(edges, N):
    distance = [ 0 for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            for e in edges[j]:
                next, d = e
                if distance[j] != INF and distance[next] > distance[j] + d:
                    distance[next] = distance[j] + d
                    if i == N-1:
                        return True
    return False

def testcase():
    N, M, W = list(map(int, input().split()))

    edges = [[] for _ in range(N)]

    for _ in range(M):
        s, e, t = map(int, input().split())
        edges[s-1].append([e-1, t])
        edges[e-1].append([s-1, t])

    for _ in range(W):
        s, e, t = map(int, input().split())
        edges[s-1].append([e-1, -t])
    
    if bellford(edges, N):
        print("YES")
    else:
        print("NO")


TC = int(input())
for _ in range(TC):
    testcase()