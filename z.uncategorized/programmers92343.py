


from collections import defaultdict
from copy import deepcopy

max_sheep = 0

def gogo(cur, used, sheep_num, wolf_num, can_go):
    global max_sheep

    if used[cur]: return
    used[cur] = True

    if is_wolf[cur]:
        wolf_num += 1
    else:
        sheep_num += 1
        max_sheep = max(max_sheep, sheep_num)

    if sheep_num <= wolf_num: return

    can_go.extend(E[cur])
    for next in can_go:
        gogo(next, deepcopy(used), sheep_num, wolf_num,
         can_go=[loc for loc in can_go if loc != next and not used[loc]])


def solution(info, edges):
    global is_wolf, E

    used = [False] * len(info)
    is_wolf = info
    E = defaultdict(list)

    for (p, c) in edges:
        E[p].append(c)

    gogo(0, used, 0, 0, [])

    return max_sheep



info, edges = [0,1,0,1,1,0,1,0,0,1,0],	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	
info, edges = [0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	

print(solution(info, edges))