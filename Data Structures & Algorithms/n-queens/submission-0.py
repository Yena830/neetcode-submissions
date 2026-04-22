class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        input:integer n
        output: 2d array contains 'Q' and '.' and each row each col each diagonal
                should only have one 'Q'
        P:
        1.use backtrack
        2.put the Q in each row(different col)
        3.check rows and cols and diags

        """
        queens = [0]*n
        cols = [False]*n
        diag1 = [False]*(2*n-1)
        diag2 = [False]*(2*n-1)
        res = []
        def backtrack(i):
            if i == n:
                res.append(['.'*q + 'Q' + '.'*(n-q-1) for i,q in enumerate(queens)])
                return
            for j in range(n):
                if cols[j] or diag1[i+j] or diag2[i-j+n-1]:
                    continue
                queens[i] = j
                cols[j] = True
                diag1[i+j] = True
                diag2[i-j+n-1] = True
                backtrack(i+1)
                cols[j] = False
                diag1[i+j] = False
                diag2[i-j+n-1] = False
        backtrack(0)
        return res

            