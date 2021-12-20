"""
https://programmers.co.kr/learn/courses/30/lessons/87946
피로도
"""
result = 0
def gogo(k, dun, depth=0):
    global result
    if result < depth:
        result = depth
    if k < 1:
        return
    if dun == None:
        return

    for i in range(len(dun)):
        if k >= dun[i][0]:
            gogo(k - dun[i][1], dun[:i] + dun[i+1:], depth+1)

def solution(k, dungeons):
    gogo(k, dungeons)
    answer = result
    return answer


kk = 80
dundun = [[80,20],[50,40],[30,10]]	
print(solution(kk, dundun))