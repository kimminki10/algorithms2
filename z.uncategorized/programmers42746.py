
class Node:
    def __init__(self, num: int) -> None:
        self.orig = str(num)
        self.n = str(num) * 4

    def __len__(self):
        return len(self.orig)

    def __lt__(self, b):
        for i in range(4):
            ac = self.n[i]
            bc = b.n[i]
            if ac != bc:
                return ac < bc
        return self.orig < b.orig

    def __repr__(self):
        return self.n

def solution(numbers):
    answer = ''
    
    snum = list(map(Node, numbers))
    ssnum = sorted(snum, reverse=True)
    answer = str(int(''.join([n.orig for n in ssnum])))
    return answer


n = [0, 1, 101, 1010]
re = "10"
ans = solution(n)

print(ans)
print(re == ans)