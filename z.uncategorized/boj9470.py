import sys
input = sys.stdin.readline

T = int(input())

def testcase():
    K, M, P = map(int, input().split())
    edges = [[] for _ in range(M)]
    indegree = [0] * M

    for _ in range(P):
        A, B = map(int, input().split())
        indegree[B-1] += 1
        edges[A-1].append(B-1)

    result = [0]*M
    count = [0]*M
    q = []
    for i in range(M):
        if indegree[i] == 0: 
            q.append(i)
            result[i] = 1
            count[i] = 1
    
    for i in range(M):
        if q:
            cur = q.pop(0)

            for next in edges[cur]:
                indegree[next] -= 1
                
                tmp = result[cur]
                if count[cur] > 1: tmp += 1
                
                if result[next] == tmp: count[next] += 1
                elif result[next] < tmp:
                    result[next] = tmp
                    count[next] = 1

                if indegree[next] == 0: q.append(next)
    
    tmp = result[M-1]
    if count[M-1] > 1: tmp += 1
    print(K, tmp)
    
for _ in range(T):
    testcase()