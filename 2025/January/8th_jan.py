# Count the number of possible triangles

arr=[4,6,3,7]
# possible triangles are (3,4,6) and (4,6,7) , and (3,6,7) ==> 3 triangles

def countTraingles(arr):
    arr.sort()
    n=len(arr)
    count=0
    
    # fix the largest side k
    for k in range(n-1,1,-1):
        left=0
        right=k-1

        while left<right:
            if arr[left]+arr[right]>arr[k]:
                count+=right-left
                right-=1 # as we need to check for smaller side
            else:
                left+=1 # as we need to check for larger side
    return count

print(countTraingles(arr)) # 3