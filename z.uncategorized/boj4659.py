import sys
input = sys.stdin.readline

moum = set(list('aeiou'))
zaum = set([chr(i) for i in range(ord('a'), ord('z')+1)]) - moum

def is_continuous(c, ismo):
    return (c in moum and ismo) or (c not in moum and not ismo)
        
def is_acceptable(password):
    if not (set(list(password)) & moum): 
        return False

    yeonsok_count = 1
    ismo = password[0] in moum
    before = password[0]
    for c in password[1:]:
        if is_continuous(c, ismo):
            yeonsok_count += 1
        else:
            yeonsok_count = 1
        ismo = c in moum
        #print(f"c:{c}, yc:{yeonsok_count}, ismo:{ismo}")
        
        if yeonsok_count == 3: return False
        if c not in {'e', 'o'} and before == c: return False
        before = c

    return True

while True:
    password = input().strip()
    if password == 'end': break
    middle = '' if is_acceptable(password) else 'not '

    print(f"<{password}> is {middle}acceptable.")
        