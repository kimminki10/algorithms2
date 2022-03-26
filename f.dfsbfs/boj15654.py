import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))

def permutation(l, r):
    answer = []
    def dfs(n, m, ans=[], visit=set()):
        if m == 0:
            answer.append(ans[:])
            return
        
        for next in range(n):
            if next in visit: continue
            visit.add(next)

            ans.append(next)
            dfs(n, m-1, ans, visit)

            ans.pop()
            visit.remove(next)

    dfs(len(l), r)
    for ans in answer:
        print(' '.join([str(l[i]) for i in ans]))

permutation(arr, M)