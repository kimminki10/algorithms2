"""
https://www.acmicpc.net/problem/9184
신나는 함수 실행
dynamic programming
"""

import sys
input = sys.stdin.readline

d = [ [ [ -1 for _ in range(21) ] for _ in range(21) ] for _ in range(21) ]
def wraped_w(a, b, c): 
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20: return wraped_w(20, 20, 20)
    if d[a][b][c] == -1:
        d[a][b][c] = w(a, b, c)
    return d[a][b][c]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20: return wraped_w(20, 20, 20)
    if a < b and b < c: 
        return wraped_w(a, b, c-1) + wraped_w(a, b-1, c-1) - wraped_w(a, b-1, c)
    else:
        return wraped_w(a-1, b, c) + wraped_w(a-1, b-1, c) + wraped_w(a-1, b, c-1) - wraped_w(a-1, b-1, c-1)


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    result = wraped_w(a, b, c)
    print(f"w({a}, {b}, {c}) = {result}")