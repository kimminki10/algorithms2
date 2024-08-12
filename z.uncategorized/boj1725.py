import sys
input = sys.stdin.readline

N = int(input().strip())
h = [ int(input().strip()) for _ in range(N) ] + [0]

st = []
ret = 0
for i in range(N+1):
    while st and h[st[-1]] >= h[i]:
        j = st.pop()
        width = i-st[-1]-1 if st else i
        ret = max(ret, width*h[j])
    st.append(i)

print(ret)