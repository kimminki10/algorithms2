from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [ input().rstrip()[4:-4] for _ in range(N) ]

essential = "antic"
if K < 5: 
    print(0) 
    exit(0)

a = ord('a')
l2b = lambda l: 1 << (ord(l) - a)

essential_bit = 0
for l in essential:
    essential_bit |= l2b(l)

words_bit = []
to_teach = set()
for word in words:
    wb = 0
    for l in word:
        wb |= l2b(l)
        if l not in essential:
            to_teach.add(l)
    words_bit.append(wb | essential_bit)


max_word = 0
for wb in words_bit:
    if wb & essential_bit == wb:
        max_word += 1


to_teach = sorted(list(to_teach))
for combi in combinations(to_teach, min(K-5, len(to_teach))):
    can_read = essential_bit
    for l in combi:
        can_read |= l2b(l)
    
    count = 0
    for wb in words_bit:
        if wb & can_read == wb:
            count += 1
    max_word = max(max_word, count)

print(max_word)

