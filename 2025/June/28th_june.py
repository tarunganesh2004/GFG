# Counting Elements in two arrays

a = [4, 8, 7, 5, 1]
b = [4, 48, 3, 0, 1, 1, 5]

def count_elements_brute(a, b):
    res=[]
    for i in a:
        count =0
        for j in b:
            if i>=j:
                count += 1
        res.append(count)
    return res

def count_elements_optimized(a, b):
    b.sort()
    res=[]
    def binary_search(b,target):
        left,right= 0, len(b) - 1
        ans=-1
        while left<=right:
            mid= (left + right) // 2
            if b[mid] <= target:
                ans=mid
                left = mid + 1
            else:
                right = mid-1
        return ans+1  # Return count of elements less than or equal to target
    
    for x in a:
        count = binary_search(b, x)
        res.append(count)
    return res

print(count_elements_brute(a, b))  

print(count_elements_optimized(a, b))  