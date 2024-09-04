import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N) ]
res = [0] * N

if N>2:
    res[0] = res = [(arr[0][1] + arr[0][2]-arr[1][2])//2]
    res[1:] = [arr[0][i]-res[0] for i in range(1, N)]
    print(*res)
else:
    print(1,1)
