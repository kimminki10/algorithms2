import sys
input = sys.stdin.readline

testcase = int(input().strip())
for _ in range(testcase):
    s = input().strip()
    print(f"{s[0]}{s[-1]}")