import sys
input = sys.stdin.readline

N = int(input())
build_time = [0] * N
orders = [[] for _ in range(N)]
indegree = [0] * N
for i in range(N):
    line = list(map(int, input().split()))

    build_time[i] = line[0]
    line = line[1:]
    for j in line[:-1]:
        orders[j-1].append(i)
        indegree[i] += 1

q = []
rt = [ 0 ] * N
for i in range(N):
    if indegree[i] == 0: 
        q.append(i)
        rt[i] = build_time[i]

result = [0] * N
for i in range(N):
    if q:
        cur = q.pop(0)

        result[i] = cur

        for next in orders[cur]:
            rt[next] = max(rt[next], rt[cur]+build_time[next])

            indegree[next] -= 1
            if indegree[next] == 0: q.append(next)

for r in rt:
    print(r)