import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
brr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] += brr[i][j]

for row in arr:
    print(" ".join([str(i) for i in row]))