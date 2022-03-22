import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, N) -> None:
        self.parents = [-1] * N

    def find(self, v):
        if self.parents[v] < 0:
            return v
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        self.parents[b] = a

N, M = map(int, input().split())
knum = set(list(map(int, input().split()))[1:])
uf = UnionFind(N)

party = []
for _ in range(M):
    pnum = list(map(int, input().split()))[1:]
    party.append(pnum)
    first = pnum[0]
    for p in pnum:
        uf.union(p-1, first-1)
        
new_knum = set()
for k in knum:
    new_knum.add(uf.find(k-1)+1)
    
result = 0
for pnum in party:
    for p in pnum:
        if uf.find(p-1)+1 in new_knum:
            break
    else:
        result += 1
print(result)