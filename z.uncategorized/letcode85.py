from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [list(map(int, row)) for row in matrix]
        row = len(matrix)
        col = len(matrix[0])

        dd = [[0] * (col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                dd[i+1][j+1] = dd[i+1][j] + matrix[i][j] + dd[i][j+1] - dd[i][j]

        def ss(a, b, x, y, dd):
            return dd[x][y] - dd[a-1][y] - dd[x][b-1] + dd[a-1][b-1]
        
        res = 0
        l = row*col
        for f in range(l):
            for s in range(f, l):
                a, b = f//col+1, f%col+1
                x, y = s//col+1, s%col+1
                rec = (x-a+1) * (y-b+1)
                if ss(a,b,x,y,dd) == rec:
                    res = max(res, rec)
        return res
    

print(Solution().maximalRectangle(matrix=matrix))