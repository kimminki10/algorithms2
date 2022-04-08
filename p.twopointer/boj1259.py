import sys
input = sys.stdin.readline

def is_palindrom(line):
    l = 0; r = len(line)-1

    while l < r:
        if line[l] != line[r]:
            return False
        l += 1
        r -= 1
    return True

while True:
    line = input().rstrip()
    if line == "0":
        break
    if is_palindrom(line):
        print("yes")
    else:
        print("no")