N = int(input())

def bottle(i):
    if i == 0:
        return 'no more bottles'
    elif i == 1:
        return '1 bottle'
    else:
        return f'{i} bottles'
    
for i in range(N, 0, -1):
    print(f"{bottle(i)} of beer on the wall, {bottle(i)} of beer.\nTake one down and pass it around, {bottle(i-1)} of beer on the wall.\n")
print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {bottle(N)} of beer on the wall.")