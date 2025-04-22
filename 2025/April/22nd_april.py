# Unique Number I

arr=[1,2,1,5,5]

def unique(arr):
    unique_num=0
    for i in arr:
        unique_num^=i
    return unique_num

print(unique(arr))  # Output: 2