import sys
input = sys.stdin.readline

N = int(input().rstrip())

def nextnext(v):
    if v % 3 == 0: yield v // 3
    if v % 2 == 0: yield v // 2
    if v - 1 >  0: yield v - 1

q = [(0, [N])]
visit = [0] * N
while q:
    depth, p = q.pop(0)
    cur = p[-1]

    if cur == 1:
        print(depth)
        print(' '.join([str(i) for i in p]))
        break
    
    for v in nextnext(cur):
        if visit[v] == 0:
            visit[v] = 1
            q.append((depth+1, p[:]+[v]))