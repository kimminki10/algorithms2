import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
csum = sum(C)
"""
   1,3    2,0    3,3    4,5    5,4
0  0,0   10,0   10,0   10,0   10,0
1  0,0   10,0   10,0   10,0   10,0
2  0,0   10,0   10,0   10,0   10,0
3 30,3   40,3   40,3   40,3   40,3
4 30,3   40,3   40,3   40,3   50,3
5 30,3   40,3   40,3   45,5   50,5
6 30,3   40,3   60,6   60,6   60,6
7 30,3   40,3   60,6   60,6   80,7
8 30,3   40,3   60,6   75,8   80,7
"""

d = [[[0,0] for _ in range(N+1)] for _ in range(csum+2)]
for j in range(1,N+1):
    m, c = A[j-1], C[j-1]
    for i in range(csum+1):
        if i < c:
            d[i][j][0] = d[i][j-1][0]
            d[i][j][1] = d[i][j-1][1]
        else:
            if d[i][j-1][0] < m+d[i-c][j-1][0]:
                d[i][j][0] = m+d[i-c][j-1][0]
                d[i][j][1] = c+d[i-c][j-1][1]
            else:
                d[i][j][0] = d[i][j-1][0]
                d[i][j][1] = d[i][j-1][1]

for i in range(csum+1):
    if max(d[i], key=lambda x: x[0])[0] >= M:
        print(i)
        break

