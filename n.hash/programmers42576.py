


def solution(participant, completion):
    answer = ''
    h = {}
    for c in completion:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1

    for p in participant:
        if p not in h:
            answer = p; break
        
        h[p] -= 1
        if h[p] == -1:
            answer = p; break
    
    return answer





p = ["leo", "kiki", "eden"]	
c = ["eden", "kiki"]	
r = "leo"
print(solution(p, c))