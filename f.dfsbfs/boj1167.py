import sys
input = sys.stdin.readline

v_num = int(input())
edges = [ [] for _ in range(v_num+1) ]

for _ in range(v_num):
    line = list(map(int, input().split()))
    va = line[0]
    ll = len(line)
    for vb, d in zip(line[1:ll-2:2], line[2:ll-1:2]):
        edges[va].append([vb, d])
        
def bfs(start):
    visit = [0] * (v_num+1)
    visit[start] = 1
    q = [[start,0]]

    maxlen = -1
    maxlenv = 1
    while q:
        cur = q.pop(0)
        if maxlen < cur[1]:
            maxlenv, maxlen = cur

        for e in edges[cur[0]]:
            if visit[e[0]] == 1:
                continue
            visit[e[0]] = 1
            q.append([e[0], e[1] + cur[1]])
    return maxlenv, maxlen

mv, ml = bfs(1)
mv, ml = bfs(mv)
print(ml)