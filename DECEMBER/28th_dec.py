# find triplets with sum 0

arr=[0,-1,2,-3,1]

def findTriplets(arr):
    # sort the array
    arr.sort()
    n=len(arr)
    res=[]

    for i in range(n):
        # skip the duplicates for first element
        if i>0 and arr[i]==arr[i-1]:
            continue

        # now use two pointers to find the other two elements
        left=i+1
        right=n-1
        while left<right:
            cur_sum=arr[i]+arr[left]+arr[right]
            if cur_sum==0:
                res.append([arr[i],arr[left],arr[right]])

                # skip duplicates for second element
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                # skip duplicates for third element
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left+=1
                right-=1
            elif cur_sum<0:
                left+=1
            else:
                right-=1
    return res

print(findTriplets(arr))