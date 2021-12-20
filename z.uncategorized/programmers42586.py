"""
https://programmers.co.kr/learn/courses/30/lessons/42586
기능개발 (programmers 42586)
스택/큐
bad
"""
import math

def solution(progresses, speeds):
    answer = []

    current_job_days = -1
    ret_job_num = 1
    
    for p, s in zip(progresses, speeds):
        job_day = math.ceil((100 - p) / s)
        if current_job_days == -1:
            current_job_days = job_day
        elif current_job_days >= job_day:
            ret_job_num += 1
        else:
            answer.append(ret_job_num)
            current_job_days = job_day
            ret_job_num = 1

    answer.append(ret_job_num)
    return answer


p = [93, 30, 55]
s = [1, 30, 5]
print(solution(p, s))