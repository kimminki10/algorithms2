import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = set( tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K) )
L = int(input())
larr = [ input().split() for _ in range(L) ]
snake = [(0, 0)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
didx = 0

t = 0
while True:
    t += 1
    cx, cy = snake[-1]
    dx, dy = direction[didx]
    nx, ny = cx + dx, cy + dy

    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake:
        break
    snake.append((nx, ny))
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        snake.pop(0)
    
    if larr and t == int(larr[0][0]):
        _, d = larr.pop(0)
        if d == 'L':
            didx = (didx - 1) % 4
        elif d == 'D':
            didx = (didx + 1) % 4

print(t)