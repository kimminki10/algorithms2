import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
last = set(range(1, sum(arr)+2))

mask_end = 1 << N

def subset_sum(mask):
    result = 0

    i = 0
    while mask:
        if mask & 1:
            result += arr[i]
        i += 1
        mask = mask >> 1
    return result
            

for mask in range(1, mask_end):
    s = subset_sum(mask)
    if s in last:
        last.remove(s)

print(list(last)[0])