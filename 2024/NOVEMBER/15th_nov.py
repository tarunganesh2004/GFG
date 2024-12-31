# Second Largest

arr=[12,35,1,10,34,1]

def secondLargest(arr):
    first=second=float('-inf')

    for num in arr:
        if num>first:
            second=first
            first=num

        elif num>second and num!=first:
            second=num
    
    return second

print(secondLargest(arr))