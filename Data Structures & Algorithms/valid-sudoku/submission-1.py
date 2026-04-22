class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        check rows, cols, sub-boxs
        
        """
        m = len(board)
        n = len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxs = defaultdict(set)
        for r in range(m):
            for c in range(n):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in subboxs[(r//3,c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                subboxs[(r//3,c//3)].add(num)
        return True