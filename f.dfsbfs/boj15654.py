from itertools import permutations
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

for item in permutations(arr, M):
    print(' '.join([ str(i) for i in item]))


def permu(arr, r=None):
    pool = tuple(arr)
    n = len(pool)
    r = n if r is None else r

    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n-i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return