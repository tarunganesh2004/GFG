# Largest Unblocked Submatrix

n=2
m=2
k=1

arr=[[2,2]]

# brute force, try all combinations and test
def bruteForce(n,m,arr):
    # 0=free, 1=blocked 
    grid=[[0]*m for _ in range(n)]
    for r,c in arr:

        for j in range(m):
            grid[r-1][j]=1 # blockrow
        
        for i in range(n):
            grid[i][c-1]=1 # block column
    
    ans=0

    for top in range(n):
        for left in range(m):
            for bottom in range(top,n):
                for right in range(left,n):
                    valid=True 

                    # check every cell inside rectange
                    for i in range(top,bottom+1):
                        for j in range(left,right+1):
                            if grid[i][j]==1:
                                valid=False
                                break
                        
                        if not valid:
                            break 
                    
                    if valid:
                        area=(bottom-top+1)*(right-left+1)
                        ans=max(ans,area)
    return ans 

# optimized way is instead of checking each cell
# we can find largest consecutive free rows and largest consecutive free columns 
# ans is productof these both 

# now to find largest consecutive free rows
# sort the blocked rows
# add boundaries to the blocked rows starting 0 and last n+1,
def largestArea(n,m,arr):
    blockedRows=[]
    blockedCols=[]
    for r,c in arr:
        blockedRows.append(r)
        blockedCols.append(c)
    blockedRows.sort()
    blockedCols.sort()

    maxRows=0
    # we need a previous blocked row 
    prev=0
    for row in blockedRows:
        gap=row-prev-1 # free rows b/w prev and current
        maxRows=max(gap,maxRows)
        prev=row 
    # last gap (last blocked row --> n+1)
    gap=(n+1)-prev-1
    maxRows=max(maxRows,gap)

    # same logic for blockedCols
    maxCols=0
    prev=0
    for col in blockedCols:
        gap=col-prev-1
        maxCols=max(maxCols,gap)
        prev=col 
    
    # lastgap(last blocked col-->m+1)
    gap=(m+1)-prev-1
    maxCols=max(maxCols,gap)

    return maxRows*maxCols

# another optimized version
def optimized(n,m,arr):
    def maxGap(blocked,limit):
        blocked.sort()
        blocked=[0]+blocked+[limit+1]
        ans=0

        for i  in range(1,len(blocked)):
            ans=max(ans,blocked[i]-blocked[i-1]-1)

        return ans 
    
    rows=[]
    cols=[]
    for r,c in arr:
        rows.append(r)
        cols.append(c)

    return maxGap(rows,n)*maxGap(cols,m)

print(bruteForce(n,m,arr))

print(largestArea(n,m,arr))
print(optimized(n,m,arr))