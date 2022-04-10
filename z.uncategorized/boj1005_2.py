import sys
input = sys.stdin.readline

INF = 1987654321
T = int(input())

def testcase():
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    
    indegree = [0] * N
    for _ in range(K):
        X, Y = map(int, input().split())
        indegree[Y-1] += 1
        edges[X-1].append(Y-1)
    W = int(input())

    result = [-1] * N
    q = []
    for i in range(N):
        if indegree[i] == 0: 
            result[i] = D[i]
            q.append(i)

    for i in range(N):
        if q:
            cur = q.pop(0)

            for next in edges[cur]:
                indegree[next] -= 1
                result[next] = max(result[next], result[cur] + D[next])
                if indegree[next] == 0: q.append(next)
        else:
            print(0)
            sys.exit(0)

    print(result[W-1])

for _ in range(T):
    testcase()