import sys
input = sys.stdin.readline

class QQ:
    def __init__(self) -> None:
        self.arr = []

    def push(self, v) -> None:
        self.arr.append(v)
    
    def pop(self) -> int:
        return -1 if self.empty() else self.arr.pop(0)
    
    def size(self) -> int:
        return len(self.arr)

    def empty(self) -> int:
        return 0 if self.size() else 1

    def front(self) -> int:
        return -1 if self.empty() else self.arr[0]
    
    def back(self) -> int:
        return -1 if self.empty() else self.arr[-1]

    
q = QQ()
N = int(input().strip())
for _ in range(N):
    l = input().strip()
    match l[1]:
        case 'u':
            v = int(l.split()[1])
            q.push(v)
        case 'o':
            print(q.pop())
        case 'i':
            print(q.size())
        case 'm':
            print(q.empty())
        case 'r':
            print(q.front())
        case 'a':
            print(q.back())