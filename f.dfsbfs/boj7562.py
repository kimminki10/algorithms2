"""
나이트의 이동
bfs할 때 주의사항 queue에 넣을 때 조건을 확인해서 넣어야 한다. 넣고나서 확인하면 훨씬 느리다.
"""


import sys
input = sys.stdin.readline

def is_possible(x, y, l, board):
    if x < 0 or x >= l: return False
    if y < 0 or y >= l: return False
    if board[x][y] != -1: return False
    return True

def testcase():
    length = int(input())
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())

    board = [[ -1 ] * length for _ in range(length) ]

    move = [ [-2, 1],
             [-1, 2],
             [ 1, 2],
             [ 2, 1],
             [-2,-1],
             [-1,-2],
             [ 1,-2],
             [ 2,-1] ]
             
    count = 0
    q = []
    q.append([cx,cy, count])

    while len(q) > 0:
        x, y, c = q.pop(0)
        if x == tx and y == ty: 
            print(c)
            break
        for m in move:
            if is_possible(x+m[0], y+m[1], length, board):
                board[x+m[0]][y+m[1]] = c+1
                q.append([x+m[0], y+m[1], c+1])

T = int(input())
for _ in range(T):
    testcase()
