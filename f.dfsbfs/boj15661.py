from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
jido = [list(map(int, input().split())) for _ in range(N)]

def team_synergy(team):
    score = 0
    for combi in combinations(team, 2):
        a, b = combi
        score += jido[a][b]
        score += jido[b][a]
    return score


result = 9876543210
for team_size in range(1, N//2 + 1):
    for team_start in combinations(range(N), team_size):
        team_link = list(set(range(N)) - set(team_start))

        team_start = team_synergy(team_start)
        team_link  = team_synergy(team_link)
        result = min(result, abs(team_start - team_link))

print(result)