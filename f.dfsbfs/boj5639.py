import sys
sys.setrecursionlimit(2**14)
input = sys.stdin.readline

def postpost(li):
    if li == []: return

    root = li[0]
    llen = len(li)
    if llen == 1:
        print(root)
        return
    if li[-1] < root:
        postpost(li[1:])
        print(root)
        return
    for i in range(1, llen):
        if root < li[i]:
            postpost(li[1:i])
            postpost(li[i:])
            print(root)
            break

preorder = []
while True:
    re = input()
    if re != '':
        preorder.append(int(re))
    else:
        break

postpost(preorder)

