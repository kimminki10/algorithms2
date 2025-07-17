import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    stack = []
    line = list(map(int, input().split()))
    li = 0
    order = 1
    while order <= N:
        if stack and stack[-1] == order:
            stack.pop()
            order += 1
            continue
        if stack == [] or stack[-1] > line[li]:
            stack.append(line[li])
            li += 1
        else:
            print("Sad")
            return
    print("Nice")
solve()