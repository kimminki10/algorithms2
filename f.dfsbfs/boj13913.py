import sys
sys.setrecursionlimit(2 ** 18)
input = sys.stdin.readline

N, K = map(int, input().split())

def valid(visit, x):
    if not (0 <= x <= 300_000):   return False
    if visit[x] != 0:           return False
    return True

q = [(0, N)]
visit = [0] * 300_001
visit[N] = 1
before = [-1] * 300_001
ti = 0
while q:
    ct, cp = q.pop(0)

    if cp == K:
        ti = ct
        break

    if valid(visit, cp-1): 
        visit[cp-1] = 1
        before[cp-1] = cp
        q.append((ct+1, cp-1))
    
    if valid(visit, cp+1): 
        visit[cp+1] = 1
        before[cp+1] = cp
        q.append((ct+1, cp+1))
    
    if valid(visit, cp*2): 
        visit[cp*2] = 1
        before[cp*2] = cp
        q.append((ct+1, cp*2))

def print_trace(p):
    if p == -1:
        return
    print_trace(before[p])
    print(p, end=' ')

print(ti)
print_trace(before[K])
print(K)
