import sys
input = sys.stdin.readline


N = int(input())

papa = [ 0 ] * N
edges = [[] for _ in range(N) ]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def bfs(start):
    start = start-1

    visit = [0] * N
    visit[start] = 1
    q = [start]

    while q:
        cur = q.pop(0)

        for e in edges[cur]:
            if visit[e] == 0:
                visit[e] = 1
                papa[e] = cur+1
                q.append(e)

bfs(1)

for i in papa[1:]:
    print(i)