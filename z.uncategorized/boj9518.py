import sys
input = sys.stdin.readline

r,s = map(int, input().split())
jido = [ [0]*(s+2) ]
jido += [ [0]+list(input().strip())+[0] for _ in range(r) ]
jido += [ [0]*(s+2) ]

di = [[1,0],[1,-1],[1,1],
      [0,1],[0,-1],
      [-1,0],[-1,1],[-1,-1],]

def count_shake(x,y, d):
    cnt = 0
    for a,b in d:
        if jido[x+a][y+b] == 'o':
            cnt += 1
    return cnt


ans = 0
total = 0
position = [0,0]
for i in range(r):
    for j in range(s):
        x, y = i+1, j+1
        cnt = count_shake(x,y,di)
        if jido[x][y] == 'o': 
            total += cnt
            continue
        if cnt > ans:
            ans = cnt
            position = [x,y]
ans += total//2
print(ans)