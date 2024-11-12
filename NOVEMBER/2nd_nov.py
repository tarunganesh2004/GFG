# kth Distance
# https://www.geeksforgeeks.org/problems/kth-distance3757/1

arr=[1,2,3,4,1,2,3,4]
k=3

def checkDuplicatesWithinK(arr,k):
    if k>len(arr): return False

    last_seen={}

    for i,num in enumerate(arr):
        if num in last_seen and i-last_seen[num]<=k:
            print(last_seen)
            return True
        
        last_seen[num]=i
        print(last_seen)
    return False

print(checkDuplicatesWithinK(arr,k))