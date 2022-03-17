import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v, l, r) -> None:
        self.v = v
        self.l = l
        self.r = r

N = int(input())
graph = {}
for _ in range(N):
    x, y, z = input().split()
    new_node = Node(x, y, z)
    graph[x] = new_node

def preorder(strn):
    n = graph[strn]
    print(n.v, end='')
    if n.l != '.': preorder(n.l)
    if n.r != '.': preorder(n.r)

def inorder(strn):
    n = graph[strn]
    if n.l != '.': inorder(n.l)
    print(n.v, end='')
    if n.r != '.': inorder(n.r)

def postorder(strn):
    n = graph[strn]
    if n.l != '.': postorder(n.l)
    if n.r != '.': postorder(n.r)
    print(n.v, end='')

preorder("A"); print()
inorder("A"); print()
postorder("A"); print()
