"""
https://programmers.co.kr/learn/courses/30/lessons/42587
프린터
큐
"""


def solution(priorities, location):
    answer = 0
    arr = [ (-v, v, i) for i, v in enumerate(priorities) ]
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sorted_arr[i][1] == arr[i][1]:
                break
            else:
                t = arr[i]
                del arr[i]
                arr.append(t)
    
    for i, v in enumerate(arr):
        if v[2] == location:
            answer = i+1
            break
    return answer

p = [1, 1, 9, 1, 1, 1]		
l = 0
print(solution(p, l))