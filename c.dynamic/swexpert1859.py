"""
1859 백만장자 프로젝트
"""

def best_profit():
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0

    m_i = idx = len(arr)-1
    s = 0
    while True:
        if arr[m_i] >= arr[idx-1]:
            s += arr[idx]
        else:
            s += arr[idx]
            result += (arr[m_i] * (m_i-idx+1)) - s
            m_i = idx-1
            s = 0

        idx -= 1
        if idx == -1: 
            result += (arr[m_i] * (m_i-idx)) - s
            break
        
    return result

def testcase(t):
    result = best_profit()
    print(f"#{t+1} {result}")


def solve():
    t = int(input())
    for i in range(t):
        testcase(i)

solve()