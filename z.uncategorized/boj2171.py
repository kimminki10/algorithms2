import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)])
arr_set = set(arr)
ans = 0

for i in range(N):
    x, y = arr[i]
    for j in range(i, N):
        a, b = arr[j]
        if x == a or y == b: continue
        if (x,b) in arr_set and (a,y) in arr_set:
            ans += 1
print(ans // 2)