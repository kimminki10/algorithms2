import sys
input = sys.stdin.readline


N, M = map(int, input().split())
adj = [ [] for _ in range(N) ]
indegree = [0] * N

for _ in range(M):
    line = list(map(int, input().split()))
    K = line[0]
    if K == 0: continue

    prev = line[1]
    for cur in line[2:]:
        indegree[cur-1] += 1
        adj[prev-1].append(cur-1)
        prev = cur

result = [0] * N
q = []
for i in range(N):
    if indegree[i] == 0: q.append(i)

for i in range(N):
    if q:
        cur = q.pop(0)
        result[i] = cur+1

        for next in adj[cur]:
            indegree[next] -= 1
            if indegree[next] == 0: q.append(next)
    else:
        print(0)
        sys.exit(0)
    
for i in result:
    print(i)
