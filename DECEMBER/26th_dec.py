# Two sum pair with given sum


arr=[1,4,45,6,10,8]
target=16

def twoSum(arr,target):
    map={}
    for i in arr:
        complement=target-i
        if complement in map:
            return True
        map[i]=1

    return False

print(twoSum(arr,target))