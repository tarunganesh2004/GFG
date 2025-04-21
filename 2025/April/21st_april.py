# Missing in Array 

arr=[1,2,3,5] # 4 is missing

def missing(arr):
    n=len(arr)
    total=((n+1)*(n+2))//2
    sum_of_array=sum(arr)
    return total-sum_of_array

print(missing(arr))  # Output: 4