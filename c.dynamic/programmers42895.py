
INF = 333333

def solution(N, number):
    answer = 0

    d = [[]] + [ [int(str(N) * i)] for i in range(1, 9) ]
    if [number] in d:
        return d.index([number])

    for i in range(2, 9):
        for j in range(1, i):
            for a in d[j]:
                for b in d[i-j]:
                    d[i].append(a+b)
                    d[i].append(a-b)
                    d[i].append(a*b)
                    if b != 0: d[i].append(a//b)

        if number in d[i]:
            return i
        d[i] = list(set(d[i]))
    return answer


n=5
number = 5
print(solution(n, number))