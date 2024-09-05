import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]

def is_prime(v) -> bool:
    if v < 2: return False
    for i in range(2, int(v**0.5)+1):
        if v%i == 0:
            return False
    return True

for v in arr:
    while True:
        if is_prime(v):
            print(v)
            break
        v += 1