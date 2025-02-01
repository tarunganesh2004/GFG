# Word Search

# Given a 2D board and a word, find if the word exists in the grid.

mat=[
    ['T','E','E'],
    ['S','G','K'],
    ['T','E','L']
]
word="GEEK"


# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
def isWordExist(mat,word):
    def dfs(mat,word,i,j,index):
        if index==len(word):
            return True
        if i<0 or i>=len(mat) or j<0 or j>=len(mat[0]) or mat[i][j]!=word[index]:
            return False
        temp=mat[i][j]
        mat[i][j]='#'
        found=dfs(mat,word,i+1,j,index+1) or dfs(mat,word,i-1,j,index+1) or dfs(mat,word,i,j+1,index+1) or dfs(mat,word,i,j-1,index+1)
        mat[i][j]=temp
        return found
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        for j in range(col):
            if mat[i][j]==word[0]:
                if dfs(mat,word,i,j,0):
                    return True
    return False


print(isWordExist(mat,word)) # True