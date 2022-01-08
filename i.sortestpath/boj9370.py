"""
미확인 도착지
단일-출발 최단 경로 문제
"""

import sys
input = sys.stdin.readline

def testcase():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    E = {}
    for _ in range(m):
        a, b, d = map(int, input().split())
        E[[a, b]] = d
        E[[b, a]] = d



T = int(input())
for _ in range(T):
    testcase()