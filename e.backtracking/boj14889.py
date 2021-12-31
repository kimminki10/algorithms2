"""
https://www.acmicpc.net/problem/14889
스타트와 링크
backtracking, combination, permutation
"""
import sys
input = sys.stdin.readline

from itertools import combinations, permutations

N = int(input())
S = [ [ int(i) for i in input().split() ] for _ in range(N) ]

def get_diff(st, li):
    st_sum = sum([ S[v[0]][v[1]] for v in permutations(st, 2) ])
    li_sum = sum([ S[v[0]][v[1]] for v in permutations(li, 2) ])
    return abs(st_sum-li_sum)

def solve():
    result = 987654321
    team_size = int(N/2)
    for v in combinations(range(N), team_size):
        st = list(v)
        li = [ i for i in range(N) if i not in st ]
        diff = get_diff(st,li)
        if diff < result: result = diff
    print(result)

solve()