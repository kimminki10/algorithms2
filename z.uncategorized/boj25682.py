import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
jido = [input().strip() for _ in range(N)]
BWS = 'BW'*1001


def make_correct(starts):
    correct = []
    for i in range(N):
        idx = i%2+starts
        correct.append(BWS[idx: idx+M])
    return correct


def subsum2(x,y, a,b, d):
    return d[a][b]-d[x][b]-d[a][y]+d[x][y]


def check(starts=0):
    ans = 987654321
    correct = make_correct(starts)
    
    d = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            d[i+1][j+1] = d[i+1][j] + d[i][j+1] - d[i][j]
            if correct[i][j] == jido[i][j]:
                d[i+1][j+1] += 1

    for i in range(N-K+1):
        for j in range(M-K+1):
            ans = min(ans, K*K-subsum2(i,j,i+K,j+K, d))
    return ans

print(min(check(0), check(1)))
