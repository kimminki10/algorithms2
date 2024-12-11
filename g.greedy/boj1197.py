import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, size: int):
        self.parent = [ i for i in range(size+1) ]
        self.rank = [0] * (size+1)
    
    def uu(self, a: int, b: int) -> bool:
        x,y = map(self.ff, [a,b])
        if x == y: return False
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
        return True
    
    def ff(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.ff(self.parent[x])
        return self.parent[x]

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append([c, a-1,b-1])
edges.sort()

ans = 0
uf = UnionFind(V)
for c,a,b in edges:
    if uf.uu(a,b):
        ans += c
print(ans)