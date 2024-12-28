# count pairs with given sum
arr=[1,5,7,-1,5]
target=6

def countPairs(arr,target):
    map={}
    count=0
    for i in arr:
        complement=target-i
        if complement in map:
            count+=map[complement]
        
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    return count

print(countPairs(arr,target))