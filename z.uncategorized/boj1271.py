import sys
from decimal import Decimal

n, m = map(int, sys.stdin.readline().split())

print(Decimal(n // m))
print(Decimal(n % m))