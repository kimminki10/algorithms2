import sys
input = sys.stdin.readline

def solve():
    Q = int(input())

    UP = '^'
    DOWN = 'v'

    left = -10 ** 18 -1
    right = 10 ** 18 +1
    ans = -1

    for i in range(Q):
        num, direction = input().split()
        num = int(num)

        if direction == UP:
            left = max(left, num)
        elif direction == DOWN:
            right = min(right, num)
        
        if right - left < 2:
            print('Paradox!')
            print(i+1)
            return
        if ans == -1 and right - left == 2:
            ans = i+1
    
    if right - left == 2:
        print('I got it!')
        print(ans)
        return
    else:
        print('Hmm...')

solve()