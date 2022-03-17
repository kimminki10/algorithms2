import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

inin = list(map(int, input().split()))
popo = list(map(int, input().split()))

idxidx = [ 0 ] * (n+1)
for i in range(n):
    idxidx[inin[i]] = i

def gogo(ist, ied, pst, ped):
    if ist > ied or pst > ped:
        return
    
    root = popo[ped]
    print(root, end=' ')

    left = idxidx[root] - ist
    right = ied - idxidx[root]

    gogo(ist, ist+left-1, pst, pst+left-1)
    gogo(ied-right+1, ied, ped-right, ped-1)
    
gogo(0, n-1, 0, n-1)
print()