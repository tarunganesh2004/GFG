# Majority Element

arr=[1,1,2,1,3,5,1]

def majorityElement(arr):
    count=0
    candidate=0
    for num in arr:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1

    return candidate

print(majorityElement(arr))  # Output: 1