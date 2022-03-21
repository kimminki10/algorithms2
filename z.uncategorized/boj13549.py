import sys
input = sys.stdin.readline

N, K = map(int,input().split())

result = abs(K-N)
q = [(N, 0)]
visited = [ 0 ] * 100001
t = 0
while q:
    cur, t = q.pop(0)
    visited[cur] = 1

    if cur == K: break
    
    if cur*2 <= 100000 and not visited[cur*2]: q.insert(0, (cur*2, t))
    if cur+1 <= 100000 and not visited[cur+1]: q.append((cur+1, t+1))
    if cur-1 >= 0      and not visited[cur-1]: q.append((cur-1, t+1))

print(t)