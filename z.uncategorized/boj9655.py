import sys
input = sys.stdin.readline

# 1 sec
"""
1: B
2: A
3: B
4: A
5: B
6: A
"""
N = int(input())
print("SK" if N % 2 else "CY")