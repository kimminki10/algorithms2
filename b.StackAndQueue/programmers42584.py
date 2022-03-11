

def solution(prices):
    answer = [ 0 ] * len(prices)

    st = [(0,-1)]
    for i, v in enumerate(prices):
        top_v = st[-1][0]
        while v < top_v:
            _, pi = st.pop(-1)
            top_v = st[-1][0]
            answer[pi] = i-pi
        else:
            st.append((v, i))

    st = st[1:]
    while st:
        top_v, pi = st.pop(-1)
        answer[pi] = i-pi
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))