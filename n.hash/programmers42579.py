from queue import PriorityQueue

def solution(genres, plays):
    answer = []

    g = {}
    g_sum = {}
    for i, (k, v) in enumerate(zip(genres, plays)):
        if k in g:
            g_sum[k] -= v
            g[k].put( (-v, i))
        else:
            g_sum[k] = -v
            g[k] = PriorityQueue()
            g[k].put( (-v, i) )

    gensum = sorted(g_sum.items(), key=lambda x: x[1])
    for genre, _ in gensum:
        answer.extend([ g[genre].get()[1] for _ in range(2) if not g[genre].empty() ])
    return answer


genres = ["classic", "pop"]
plays = [500, 600]
print(solution(genres, plays))