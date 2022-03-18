
def oneone():
    i = 0
    for _ in range(10000):
        i = (i % 5) + 1
        yield i

def twotwo():
    i = 0
    for j in range(10000):
        if j % 2 == 0:
            yield 2
        else:
            i = (i % 5) + 1
            if i == 2:
                i += 1
            yield i

def threethree():
    arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    while True:
        yield from arr

def solution(answers):
    answer = []
    x = y = z = 0
    alen = len(answers)
    for i, (a, b, c) in enumerate(zip(oneone(), twotwo(), threethree())):
        if i >= alen: break
        v = answers[i]
        if a==v: x += 1
        if b==v: y += 1
        if c==v: z += 1
    
    
    m = max([x,y,z])
    for i, v in enumerate([x,y,z]):
        if v == m:
            answer.append(i+1)
    return answer

arr = [1,3,2,4,2]
print(solution(arr))