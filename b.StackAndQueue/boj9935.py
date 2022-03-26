import sys
input = sys.stdin.readline

line = input().strip()
bomb = input().strip()

st = []
i = 0
llen = len(line)
blen = len(bomb)
lbomb = list(bomb)

while True:
    if i >= llen: break
    st.append(line[i])

    if line[i] == bomb[-1]:
        if st[-blen:] == lbomb:
            for _ in range(blen):
                st.pop()
    i+=1

line = ''.join(st)
if line == '':
    print("FRULA")
else:
    print(line)