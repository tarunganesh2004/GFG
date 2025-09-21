# Max Rectangle 

mat=[[0, 1, 1, 0],
     [1, 1, 1, 1],
     [1,1,1,1],
     [1,1,0,0]]

def maximalRectangle(matrix):
    # def largest_rectangle_histogram(heights): # O(n^2)
    #     n=len(heights)
    #     max_area=0
    #     for i in range(n):
    #         height=heights[i]

    #         # look left
    #         left=i 
    #         while left-1>=0 and heights[left-1]>=height:
    #             left-=1
    #         # look right
    #         right=i
    #         while right+1<n and heights[right+1]>=height:
    #             right+=1
            
    #         # width is number of columns from left to right inclusive 
    #         width=right-left+1
    #         area=width*height
    #         max_area=max(max_area,area)
    #     return max_area

    def largest_rectangle_histogram(heights): # O(n)
        stack=[]
        max_area=0
        heights.append(0) # sentinel
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h=heights[stack.pop()]
                w=i if not stack else i-stack[-1]-1
                max_area=max(max_area,h*w)
            stack.append(i)
        heights.pop() # remove sentinel
        return max_area

    m=len(matrix)
    n=len(matrix[0]) if m>0 else 0

    # heights array 
    # for each column it stores how many consecutive 1’s are stacked vertically up to the current row.
    heights=[0]*n
    max_area=0
    for r in range(m):
        for c in range(n):
            if matrix[r][c]==1:
                heights[c]+=1
            else:
                heights[c]=0
                
        # now we need to find largest rectangle in histogram for each row
        area=largest_rectangle_histogram(heights)
        max_area=max(max_area,area)
    
    return max_area


print(maximalRectangle(mat))