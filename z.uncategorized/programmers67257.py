

from copy import deepcopy
from itertools import permutations


def atoi(s):
    ret = ''
    for c in s:
        if '0' <= c <= '9':
            ret += c
        else: break
    return ret

def calc(a, b, op):
    a = int(a); b = int(b)
    if op == '-': return a - b
    if op == '+': return a + b
    if op == '*': return a * b

def eval(order, idx, l):
    if len(order) == idx:
        return l[0]
    op = order[idx]

    i = 1
    while i < len(l)-1:
        if op == l[i]:
            num = calc(l[i-1], l[i+1], l[i])
            i -= 1
            l.pop(i)
            l.pop(i)
            l.pop(i)
            l.insert(i, num)
        i += 1
    return eval(order, idx+1, l)
        

def solution(expression):
    answer = 0

    l = []

    i = 0
    while i < len(expression):
        num = atoi(expression[i:])
        l.append(num)
        i += len(num)
        if i >= len(expression): break
        l.append(expression[i])
        i += 1
    
    op_list = ['-', '+', '*']

    for c in permutations(op_list):
        answer = max(answer, abs(eval(c, 0, deepcopy(l))))
    
    return answer


expression = "100-200*300-500+20"
print(solution(expression))