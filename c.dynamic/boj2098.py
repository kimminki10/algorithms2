import sys
input = sys.stdin.readline

INF = 987654321
N = int(input())
jido = [ list(map(int, input().split())) for _ in range(N)]

def is_bit_off(i, visit):
    return visit & (1 << i) == 0

cost = [[-1] * (1 << 16) for _ in range(N)]
allset = (1 << N) -1
def dfs(cur, visit):
    if cost[cur][visit] != -1:
        return cost[cur][visit]

    if visit == allset:
        if jido[cur][0] == 0:
            return INF
        else:
            return jido[cur][0]
    
    cost[cur][visit] = INF
    for i, c in enumerate(jido[cur]):
        if c == 0 or (not is_bit_off(i, visit)):
            continue
        cost[cur][visit] = min(cost[cur][visit], dfs(i, visit | (1<<i)) + jido[cur][i])
    return cost[cur][visit]

print(dfs(0, 1))
        