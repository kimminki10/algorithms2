from collections import defaultdict
import sys
input = sys.stdin.readline


def make_key(key):
    result = [[''] * 5 for _ in range(5)]
    idx = 0

    d = dict()
    for i in range(ord('A'), ord('Z')+1):
        d[chr(i)] = 1
    d.pop('J')

    for word in list(key):
        if word in d:
            y = idx % 5
            x = idx // 5

            result[x][y] = word
            idx += 1
            d.pop(word)
    
    for i in range(ord('A'), ord('Z')+1):
        word = chr(i)
        if word in d:
            y = idx % 5
            x = idx // 5

            result[x][y] = word
            idx += 1
            d.pop(word)
    return result


def split_two_words(message):
    result = ""
    idx = 0
    while idx < len(message)-1:
        f, s = message[idx], message[idx+1]
        if f == s:
            result += f
            if f == 'X':
                result += 'Q'
            else:
                result += 'X'
            idx += 1
        else:
            result += f + s
            idx += 2

    while idx < len(message):
        result += message[idx]
        idx += 1
    if len(result) % 2 == 1:
        result += 'X'

    return result


def get_cord(key, w):
    for i, row in enumerate(key):
        for j, v in enumerate(row):
            if v == w:
                return i, j



def solve():
    message = input().rstrip()
    key = input().rstrip()

    key = make_key(key)
    message = split_two_words(message)

    result = ""
    for i in range(0, len(message), 2):
        m = message[i: i+2]
        fx, fy = get_cord(key, m[0])
        sx, sy = get_cord(key, m[1])

        if fx == sx:
            fy = (fy + 1) % 5
            sy = (sy + 1) % 5
        elif fy == sy:
            fx = (fx + 1) % 5
            sx = (sx + 1) % 5
        else:
            fy, sy = sy, fy
        result += key[fx][fy] + key[sx][sy]
    return result

print(solve())