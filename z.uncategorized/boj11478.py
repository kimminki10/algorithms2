import sys
input = sys.stdin.readline

S = input().strip()
slen = len(S)
subsets = set()
for length in range(1, slen+1):
    for i in range(slen):
        subsets.add(S[i: i+length])

print(len(subsets))