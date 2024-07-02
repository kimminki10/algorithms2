import sys
input = sys.stdin.readline

good = [1,1,2,2,2,8]
l = map(int, input().split())

print(" ".join([ str(b-a) for a, b in zip(l, good) ]))
