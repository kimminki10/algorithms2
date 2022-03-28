import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = [ 987654321 ] * 100001 # time

def gogo(cur_time, next):
    global d, q
    if not 0<= next <= 100000: return
    if cur_time < d[next]:
        d[next] = cur_time
        q.append(next)

d[N] = 0
q = [N]
while q:
    X = q.pop(0)

    if X == K:
        break
    cur_time = d[X]+1
    gogo(cur_time, X*2)
    gogo(cur_time, X+1)
    gogo(cur_time, X-1)

print(d[K])