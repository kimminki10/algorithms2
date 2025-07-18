import sys
input = sys.stdin.readline

n = int(input())
tree = [list(map(int,input().split())) for _ in range(n)]

for r in range(n-1,0,-1):
    for c in range(len(tree[r])-1):
        tree[r-1][c] += max(tree[r][c],tree[r][c+1])

print(tree[0][0])