import sys
input = sys.stdin.readline

rmin = '9876543210'
rmax = '0'

def answer_control(l):
    global rmin, rmax
    num = ''.join([str(i) for i in l])
    rmin = min(num, rmin)
    rmax = max(num, rmax)


def dfs(idx, answer, check, visit):
    if idx == len(check):
        answer_control(answer)
        return
    
    prev = answer[-1]
    if check[idx]:
        for i in range(prev, 10):
            if visit[i] == 0:
                visit[i] = 1
                dfs(idx+1, answer + [i], check, visit)
                visit[i] = 0
    else:
        for i in range(prev):
            if visit[i] == 0:
                visit[i] = 1
                dfs(idx+1, answer + [i], check, visit)
                visit[i] = 0


def solve():
    k = int(input())
    line = input().rstrip().split()

    is_greater_than = [ l == "<" for l in line ]

    visit = [0] * 10
    for i in range(10):
        visit[i] = 1
        dfs(0, [i], is_greater_than, visit)
        visit[i] = 0
    
    print(rmax)
    print(rmin)

solve()