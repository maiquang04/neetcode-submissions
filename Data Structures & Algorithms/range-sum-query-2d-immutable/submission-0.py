class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = defaultdict(int)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x = (row1, col1, row2, col2)
        if x in self.m:
            return self.m[x]
        
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.m[x] += self.matrix[i][j]

        return self.m[x]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)