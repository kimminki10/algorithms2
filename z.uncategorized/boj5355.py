import sys
input = sys.stdin.readline
T = int(input().strip())

def testcase():
    l = input().split()
    result = float(l[0])

    for v in l[1:]:
        match v:
            case '@': result*=3
            case '%': result+=5
            case '#': result-=7
    return result

for _ in range(T):
    print(f"{testcase():.2f}")