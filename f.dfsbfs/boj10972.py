import sys
input = sys.stdin.readline


N = int(input().rstrip())
arr = list(map(int, input().split()))


def next_permu(arr, n):
    i = n-1
    while i > 0 and arr[i-1] >= arr[i]: i -= 1

    if i <= 0: return False
    j = n-1
    while arr[j] <= arr[i-1]: j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    j = n-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True

if next_permu(arr, N):
    print(' '.join(map(str, arr)))
else: print('-1')