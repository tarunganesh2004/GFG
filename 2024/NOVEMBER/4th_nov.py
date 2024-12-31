# Find All Triplets with zero sum

arr=[0, -1, 2, -3, 1]

def findTriplets(arr):
    n=len(arr)
    res=[]
    for i in range(n-2):
        seen={}
        for j in range(i+1,n):
            x=-(arr[i]+arr[j])
            if x in seen:
                res.append(sorted([seen[x],i,j]))
            else:
                seen[arr[j]]=j

    return res

print(findTriplets(arr))