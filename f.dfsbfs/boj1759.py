from itertools import combinations
import sys
input = sys.stdin.readline


L, C = map(int , input().split())
arr = input().split()
arr.sort()

moum_list = 'aeiou'
moum = []
jaum = []
for i in arr:
    if i in moum_list:
        moum.append(i)
    else:
        jaum.append(i)

result = []
moum_len = len(moum)
for m_count in range(1, moum_len+1):
    if L-m_count < 2: continue
    
    moum_combi = list(combinations(moum, m_count))
    for c in combinations(jaum, L-m_count):
        for moum_select in moum_combi:
            item = list(c + moum_select)
            item.sort()
            result.append(item)
    
result.sort()
for row in result:
    print(''.join(row))
