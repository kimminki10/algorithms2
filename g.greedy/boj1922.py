import sys
input = sys.stdin.readline

def getline():
    return map(int, input().split())

class UnionFind:
    def __init__(self, size) -> None:
        self.parents = [ -1 ] * size

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)    

        if a == b: return False
        self.parents[b] = a
        return True

V = int(input())
E = int(input())
edges = []
for _ in range(E):
    a, b, c = getline()
    edges.append((a-1, b-1, c))

uf = UnionFind(V)
edges.sort(key=lambda x: x[2])

result = 0
cnt = 0
for e in edges:
    if uf.union(e[0], e[1]):
        result += e[2]
        cnt += 1
        if cnt == V-1: break
print(result)