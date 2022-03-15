from bisect import bisect_left as bl

def solution(citations):
    answer = 0

    lc = len(citations)
    sc = sorted(citations)
    print(sc)
    for inyong in range(lc+1):
        bidx = bl(sc, inyong)
        inyong_num = lc-bidx

        print(inyong, bidx, sc[bidx], inyong_num)
        if inyong <= inyong_num:
            answer = inyong
    return answer


c = [3, 0, 6, 1, 5]	
print(solution(c))