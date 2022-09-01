from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
jido = [list(map(int, input().split())) for _ in range(N)]

def calc_cost(path):
    res = 0
    st = path[0]
    for en in path[1:]:
        if jido[st][en] == 0:
            return 987654321
        res += jido[st][en]
        st = en
    return res


answer = 9876543210
for perm in permutations(range(N)):
    answer = min(answer, calc_cost(list(perm) + [perm[0]]))
print(answer)