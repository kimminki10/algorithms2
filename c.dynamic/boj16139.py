import sys
input = sys.stdin.readline

s = input().rstrip()
d = [[0] * (len(s)+1) for _ in range(26)]

for j, c in enumerate(s):
    d[ord(c) - ord('a')][j] += 1
    for i in range(26):
        d[i][j+1] += d[i][j]

for i in range(26):
    d[i].insert(0, 0)
q = int(input())

def question():
    c, st, en = input().split()
    c = ord(c) - ord('a')
    st = int(st)
    en = int(en)
    print(d[c][en+1] - d[c][st])


for i in range(q):
    question()
