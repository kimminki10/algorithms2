import sys
input = sys.stdin.readline

def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)


a, b = map(int, input().split())
c, d = map(int, input().split())

x = a*d + c*b
y = b*d

div = gcd(x,y)
print(x//div, y//div)