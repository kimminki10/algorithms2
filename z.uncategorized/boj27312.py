import sys
input = sys.stdin.readline

M,N,Q = map(int, input().split())
arr = list(map(int, input().split()))

result = [set(i+1 for i in range(x)) for x in arr]

for i in range(Q):
    print(" ".join(["?"] + [str(i%M + 1), str(i%N + 1)]))
    sys.stdout.flush()

    ans = int(input().strip())
    result[i].remove(ans)

print("! "+" ".join([ str(i.pop()) for i in result ]))
sys.stdout.flush()