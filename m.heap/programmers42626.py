import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K: break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + b * 2
        heapq.heappush(scoville, c)
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        answer += 1

    return answer


sc, k = [1, 2, 3, 9, 10, 12],	7
print(solution(sc, k))