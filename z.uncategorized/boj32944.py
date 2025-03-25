import sys
input = sys.stdin.readline

"""
2 <= N <= 300000
1 <= K < M <= N

5 4 3
1 2 5 3 4

5 4 2
1 5 2 3 4

5 4 1
5 1 2 3 4

5 3 2
1 5 4 2 3

5 3 3
1 4 5 2 3

5 3 1
5 4 1 2 3
"""
def solve2(N, M, K):
    if N == M:
        return [-1]
    answer = [*range(1, K)]
    answer.append(N)
    answer.extend(range(K, M))
    answer.append(N-1)
    answer.extend(range(N-2, M-1, -1))
    return answer



def test_solve():
    input_list = [
        (5, 4, 3),
        (5, 4, 2),
        (5, 4, 1),
        (5, 3, 2),
        (5, 3, 3),
        (5, 3, 1),
        (3, 3, 2),
    ]
    res_list = [
        [1, 2, 5, 3, 4],
        [1, 5, 2, 3, 4],
        [5, 1, 2, 3, 4],
        [1, 5, 4, 2, 3],
        [1, 2, 5, 4, 3],
        [5, 4, 1, 2, 3],
        [-1],
    ]
    for inputs, res_list in zip(input_list, res_list):
        if solve(*inputs) != res_list:
            print("FAILED")
            print(inputs)
            print('ans', res_list)
            print('res', solve(*inputs))
            break


def solve(N, M, K):
    if N == M:
        return [-1]
    diff = N-M
    answer = list(range(1, N+1))
    right = answer[-diff:]
    right.reverse()
    left = answer[:-diff]
    answer = left[:K-1] + right + left[K-1:]
    return answer

inputs = map(int, input().split())
print(*solve(*inputs))