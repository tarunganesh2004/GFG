# N Queens

n=4

def nQueens(n):
    board=[["."]*n for _ in range(n)]
    cols=set()
    pos_diag=set()
    neg_diag=set()

    res=[]

    def backtrack(r):
        if r==n:
            sol=[]
            for row in board:
                sol.append(row.index("Q")+1)
            res.append(sol)
            return
        
        for c in range(n):
            if c in cols or r+c in pos_diag or r-c in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            board[r][c]="Q"
            
            backtrack(r+1)

            cols.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c]="."

    backtrack(0)

    return res

print(nQueens(n))