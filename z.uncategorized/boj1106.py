import sys
input = sys.stdin.readline

C, N = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)])

d = [0] * (100005)
# d[i] : i 비용을 사용할 때 최대 얻는 사람수
for w,v in A:
    for i in range(100005):
        if i >= w:
            d[i] = max(d[i], d[i-w]+v)

for i in range(100005):
    if d[i] >= C:
        print(i)
        break