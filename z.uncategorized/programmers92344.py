
ATTACK = 1

def add_board(board, x, y, a, b, p):
    board[x][y] += p
    board[a][y] += -p
    board[x][b] += -p
    board[a][b] += p
    return board

def solution(board, skill):
    answer = 0
    sm = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for (t, x, y, a, b, p) in skill:
        if t == ATTACK:
            sm = add_board(sm, x, y, a+1, b+1, -p)
        else:
            sm = add_board(sm, x, y, a+1, b+1, p)

    for j in range(len(board[0]) + 1):
        for i in range(len(board)):
            sm[i+1][j] += sm[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            sm[i][j+1] += sm[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += sm[i][j]

    for row in board:
        for v in row:
            if v > 0:
                answer += 1
    return answer


board, skill = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	
board, skill = [[1,2,3],[4,5,6],[7,8,9]],	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))