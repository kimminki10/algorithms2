
from collections import defaultdict

def is_possible(gems, m, count):
    c = defaultdict(lambda: 0)
    i = j = 0
    while j < m:
        c[gems[j]] += 1
        j += 1

    while j < len(gems):
        if c.keys() == count.keys():
            return True, i, j-1
        
        c[gems[i]] -= 1
        if c[gems[i]] == 0: c.pop(gems[i])
        c[gems[j]] += 1
        j += 1
        i += 1
    if c.keys() == count.keys():
        return True, i, j-1
    return False, i, j


def solution(gems):
    answer = []
    count = defaultdict(lambda: 0)
    for g in gems:
        count[g] += 1
    
    l = len(count.keys()); r = len(gems); m = 0
    while l <= r:
        m = (r + l) // 2
        possible, x, y = is_possible(gems, m, count)
        if possible:
            answer = [x+1, y+1]
            r = m - 1
        else: l = m + 1
    
    return answer


ins = [
    [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],[3, 7]],
    [["AA", "AB", "AC", "AA", "AC"],[1, 3]],
    [["XYZ", "XYZ", "XYZ"],[1, 1]],
    [["ZZZ", "YYY", "NNNN", "YYY", "BBB"],[1, 5]],
    [["NNNN", "ZZZ", "YYY", "NNNN", "YYY", "BBB"],[2, 6]],
    [["B", "A", "A", "C", "A", "B", "C"],[4, 6]],
]

for (gems, ans) in ins:
    print(gems, ans)
    res = solution(gems)
    print(res, res == ans)
    