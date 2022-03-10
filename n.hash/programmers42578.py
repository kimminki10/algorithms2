


def solution(clothes):
    answer = 0

    h = {}
    for v, k in clothes:
        if k not in h:
            h[k] = [v]
        else:
            h[k].append(v)
    return answer


