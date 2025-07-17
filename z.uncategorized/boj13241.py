
def GCD(m, n):
    while n != 0:
        mod = m % n
        m, n = n, mod
    return m


a, b = map(int, input().split())
print(a * b // GCD(a,b))