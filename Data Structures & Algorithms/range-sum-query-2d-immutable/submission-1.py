class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.m = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(1, r + 1):
            p = 0
            for j in range(1, c + 1):
                above = self.m[i - 1][j]
                p += matrix[i - 1][j - 1]
                self.m[i][j] += p + above
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        whole = self.m[r2][c2]
        above = self.m[r1 - 1][c2]
        left = self.m[r2][c1 - 1]
        topleft = self.m[r1 - 1][c1 - 1]

        return whole - above - left + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)