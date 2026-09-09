class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d == ".":
                    continue
                
                pos = (i // 3, j // 3)
                if d in rows[i] or d in cols[j] or d in squares[pos]:
                    return False
                
                rows[i].add(d)
                cols[j].add(d)
                squares[pos].add(d)
        
        return True