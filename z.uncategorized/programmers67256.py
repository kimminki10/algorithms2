
def distance(cur, next):
    ret = 0
    if next == 2:
        if   cur in [1,3,5]: ret = 1
        elif cur in [4,6,8]: ret = 2
        elif cur in [7,9,0]: ret = 3
        elif cur in [-1]:    ret = 4
    if next == 5:
        if   cur in [1,3,7,9,0]: ret = 2
        elif cur in [4,6,2,8]:   ret = 1
        elif cur in [-1]:        ret = 3
    if next == 8:
        if   cur in [1,3]: ret = 3
        elif cur in [4,6,2,-1]: ret = 2
        elif cur in [7,9,5,0]: ret = 1
    if next == 0:
        if   cur in [1,3]: ret = 4
        elif cur in [4,6,2]: ret = 3
        elif cur in [7,9,5]: ret = 2
        elif cur in [8,-1]: ret = 1
    return ret

def solution(numbers, hand):
    answer = ''

    l = -1; r = -1
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            l = num
        elif num in [3, 6, 9]:
            answer += "R"
            r = num
        else:
            ld = distance(l, num)
            rd = distance(r, num)
            if ld > rd:
                r = num
                answer += "R"
            elif ld < rd:
                l = num
                answer += "L"
            else:
                if hand == "right":
                    answer += "R"
                    r = num
                else:
                    answer += "L"
                    l = num
        
    return answer

numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"
numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"
numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"
print(solution(numbers, hand))