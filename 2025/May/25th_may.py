# pythagorean triplet

arr=[3,2,4,6,5]

def find_pythagorean_triplet(arr):
    n = len(arr)
    arr.sort()
    
    for i in range(n-1, 1, -1):
        left = 0
        right = i - 1
        
        while left < right:
            if arr[left]**2 + arr[right]**2 == arr[i]**2:
                return True
            elif arr[left]**2 + arr[right]**2 < arr[i]**2:
                left += 1
            else:
                right -= 1
            
    return False

# other way
def another_way(arr):
    squared= [x**2 for x in arr]
    squared_set = set(squared)
    n=len(squared)
    for i in range(n):
        for j in range(i+1, n):
            if squared[i] + squared[j] in squared_set:
                return True
    return False

print(find_pythagorean_triplet(arr))

