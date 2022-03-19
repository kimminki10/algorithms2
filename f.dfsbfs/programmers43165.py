count = 0

def dfs(cur, target, depth, numbers, nlen):
    global count

    if depth == nlen-1:
        if cur == target:
            count += 1
        return

    depth += 1
    dfs(cur+numbers[depth], target, depth, numbers, nlen)
    dfs(cur-numbers[depth], target, depth, numbers, nlen)

def solution(numbers, target):
    answer = 0

    numbers = [0] + numbers
    dfs(0, target, 0, numbers, len(numbers))
    answer = count
    return answer


numbers, target = [4, 1, 2, 1], 4
print(solution(numbers, target))