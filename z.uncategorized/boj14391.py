import sys
input = sys.stdin.readline


# 1은 가로 0은 세로
def calc_score(mask, jido):
    check = 0
    score = 0
    
    for i in range(N * M):
        if check & (1 << i): continue

        cur_score = jido[i // M][i % M]
        if mask & (1 << i):
            j = i + 1
            x = i // M
            while j < (x + 1) * M:
                if mask & (1 << j):
                    check |= (1 << j)
                    cur_score += jido[j // M][j % M]
                else: break
                j += 1
        else:
            j = i + M
            while j < N * M:
                if (mask & (1 << j)) == 0:
                    check |= (1 << j)
                    cur_score += jido[j // M][j % M]
                else: break
                j += M    
        score += int(cur_score)

    return score

def solve(N, M, jido):
    size = 1 << (N * M)
    result = 0
    for i in range(size):
        result = max(result, calc_score(i, jido))

    return result


N, M = map(int, input().split())
jido = list(input().rstrip() for _ in range(N))

print(solve(N, M, jido))