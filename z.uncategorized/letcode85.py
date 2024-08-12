class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dd = [[0] * (col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                dd[i+1][j+1] = dd[i+1][j] + int(matrix[i][j]) + dd[i][j+1] - dd[i][j]
        
        res = 0
        for a in range(1, row+1):
            for b in range(1, col+1):
                if matrix[a-1][b-1] == "0": continue
                for x in range(a, row+1):
                    for y in range(b, col+1):
                        if matrix[x-1][y-1] == "0": break
                        ss = dd[x][y] - dd[a-1][y] - dd[x][b-1] + dd[a-1][b-1]
                        rec = (x-a+1) * (y-b+1)
                        if rec == ss:
                            if res < rec: res = rec
                        else:
                            break
                    if (row-a+1) * (y-b+1) < res:
                        break
        return res