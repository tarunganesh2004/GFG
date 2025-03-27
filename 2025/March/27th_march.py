# Minimum Platforms

arr=[900, 940, 950, 1100, 1500, 1800]
dep=[910, 1200, 1120, 1130, 1900, 2000]

# brute force
def brute_force(arr,dep):
    n=len(arr)
    res=1
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if arr[j]<=dep[i] and dep[j]>=arr[i]:
                count+=1
        res=max(res,count)
    return res



print(brute_force(arr,dep)) # 3
