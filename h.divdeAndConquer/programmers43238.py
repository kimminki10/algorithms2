
def is_possible(m, n, times):
    re = 0
    for t in times:
        re += m // t
        if re >= n:
            return True
    return False

def solution(n, times):
    answer = 0
    times.sort()

    l=0; r=1_000_000_000_000_000; m=0
    while l <= r:
        m = (l+r)//2
        if is_possible(m, n, times):
            answer = m
            r = m-1
        else:
            l = m+1
    return answer

n, times = 6, [2, 7, 10]
print(solution(n, times))
