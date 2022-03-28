import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = [ 987654321 ] * 100001 # time
count = [ 0 ] * 100001

def gogo(cur_time, X, next):
    global d, q
    if not 0 <= next <= 100000: return

    if cur_time < d[next]:
        d[next] = cur_time
        count[next] += count[X]
        q.append(next)
    elif cur_time == d[next]:
        count[next] += count[X]

d[N] = 0
count[N] = 1
q = [N]
while q:
    X = q.pop(0)

    if X == K:
        continue
    cur_time = d[X]+1
    gogo(cur_time, X, X*2)
    gogo(cur_time, X, X+1)
    gogo(cur_time, X, X-1)

print(d[K])
print(count[K])