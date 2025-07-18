from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def testcase():
    M = int(input())

    arr = []
    for _ in range((M+10)//10):
        arr.extend(list(map(int,input().split())))

    left = []
    right = []

    count = (M+1)//2
    toprint = []
    for i, v in enumerate(arr):
        heappush(left, -v)
        while len(left) > len(right)+2:
            l = -heappop(left)
            heappush(right, l)
            while left and right and -left[0] > right[0]:
                heappush(left, -heappop(right))
        if i%2 == 0: toprint.append(-left[0])
    
    print(count)
    for i in range(0, count, 10):
        print(' '.join(map(str, toprint[i:i+10])))


T = int(input())
for _ in range(T):
    testcase()