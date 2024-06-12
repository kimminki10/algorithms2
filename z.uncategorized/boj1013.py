import re
import sys
input = sys.stdin.readline



def testcase():
    line = input().strip()
    print("YES" if re.fullmatch("(100+1+|01)+", line) else "NO")
    
c = int(input())
for _ in range(c):
    testcase()