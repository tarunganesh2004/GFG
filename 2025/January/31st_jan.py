# Solve the sudoku


class Solution:
    def solveSudoku(self, mat):
        def isSafe(r, c, n):
            for i in range(9):
                if mat[r][i] == n or mat[i][c] == n:
                    return False
            r -= r % 3
            c -= c % 3
            for i in range(3):
                for j in range(3):
                    if mat[i + r][j + c] == n:
                        return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if mat[i][j] == 0:
                        for n in range(1, 10):
                            if isSafe(i, j, n):
                                mat[i][j] = n
                                if solve():
                                    return True
                                mat[i][j] = 0
                        return False
            return True

        solve()  


mat = [
    [3, 0, 6, 5, 7, 8, 4, 0, 0],
    [5, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

s = Solution()
s.solveSudoku(mat)

for row in mat:
    print(" ".join(map(str, row)))
