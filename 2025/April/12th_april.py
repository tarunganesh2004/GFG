# FLood Fill ALgorithm

image=[[1,1,1,0],[0,1,1,1],[1,0,1,1]]
sr=1
sc=2
newColor=2

def floodFill(image,sr,sc,newColor):
    if image[sr][sc] == newColor:
        return image
    oldColor = image[sr][sc]
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != oldColor:
            return
        image[r][c] = newColor
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    dfs(sr, sc)
    return image

print(floodFill(image, sr, sc, newColor))  # Output: [[2, 2, 2, 0], [0, 2, 2, 2], [1, 0, 1, 1]]