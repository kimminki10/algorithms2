from itertools import combinations
import math
import sys
input = sys.stdin.readline

T = int(input())
    
def testcase():
    minv = 98765432198765321.0
    N = int(input())
    P = []
    total_x = 0
    total_y = 0
    for _ in range(N):
        a, b = map(int, input().split())
        total_x += a
        total_y += b
        P.append((a, b))

    com = list(combinations(P, N//2))
    com_len = len(com)//2

    for e in com[:com_len]:
        x1_total = 0
        y1_total = 0
        for (x, y) in e:
            x1_total += x
            y1_total += y
        
        x2_total = total_x - x1_total
        y2_total = total_y - y1_total

        minv = min((x1_total-x2_total) ** 2 + (y1_total-y2_total) ** 2, minv)
    print(math.sqrt(minv))


for _ in range(T):
    testcase()
