import sys
input = sys.stdin.readline


n = int(input().rstrip())
arr = list(map(int, input().split()))
x = int(input().rstrip())

arr.sort()
result = 0
i = 0; j = n-1
while i < j:
    ss = arr[i] + arr[j]
    if ss == x:
        result += 1
    
    if ss > x:
        j -= 1
    else:
        i += 1

print(result)
