

parents = []
rank = [1]
def unionunion(a, b):
    a = findfind(a)
    b = findfind(b)
    if a == b:
        return

    if rank[a] < rank[b]:
        a,b = b,a
    parents[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1

def findfind(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = findfind(parents[a])
        return parents[a]

def solution(n, computers):
    global parents, rank
    parents = [ i for i in range(n) ]
    rank = [1] * n

    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                unionunion(i, j)

    for i in range(n):
        parents[i] = findfind(i)

    answer = len(set(parents))
    return answer



n, computers = 4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
print(solution(n, computers))