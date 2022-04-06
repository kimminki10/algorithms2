import sys
input = sys.stdin.readline

N, M = map(int, input().split())
orders = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    indegree[b-1] += 1
    orders[a-1].append(b-1)

result = [0] * N
q = []
for i in range(N):
    if indegree[i] == 0: q.append(i)

for i in range(N):
    if q:
        cur = q.pop(0)
        result[i] = cur+1

        for next in orders[cur]:
            indegree[next] -= 1
            if indegree[next] == 0: q.append(next)

print(' '.join([str(i) for i in result]))