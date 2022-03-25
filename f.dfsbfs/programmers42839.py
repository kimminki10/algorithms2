from itertools import permutations
def is_prime(n):
    if n < 2: return False
    if n == 2: return True

    m = int(n ** (1/2))+1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    idxs = list(range(len(numbers)))

    num_set = set()
    for r in range(1, len(numbers)+1):
        for nums in permutations(idxs, r):
            num = ''.join([numbers[i] for i in nums])
            num_set.add(int(num))

    num_set = sorted(num_set)
    for n in num_set:
        if is_prime(n):
            answer += 1
    return answer

print(solution("1231"))