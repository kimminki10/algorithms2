import sys
input = sys.stdin.readline

d = [[0] * 3 for _ in range(100001)]
d[1] = [1,0,0]
d[2] = [0,1,0]
d[3] = [1,1,1]

for i in range(4, 100001):
    d[i][0] = (d[i-1][1]+d[i-1][2]) % 1000000009
    d[i][1] = (d[i-2][0]+d[i-2][2]) % 1000000009
    d[i][2] = (d[i-3][0]+d[i-3][1]) % 1000000009


T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    print(sum(d[n]) % 1000000009)