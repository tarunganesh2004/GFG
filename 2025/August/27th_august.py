# Count the Number of Possible Triangles

arr=[4,6,3,7]

def findNumberOfTriangles(arr):
    n=len(arr)
    arr.sort()
    count = 0
    for i in range(n-1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] > arr[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1
    return count

print(findNumberOfTriangles(arr))