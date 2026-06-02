arr=[-1,0,-2,4,3]
arr1=[-1,0]
def findMaxProduct(arr):
    # n=len(arr)
    # mod=1e9+7
    # res=1
    # ne=[]
    # for i,num in enumerate(arr):
    #     if num<0:
    #         ne.append(num)
    
    # ne.sort()
    # if len(ne)%2==0:
    #     for n1 in ne:
    #         res*=n1 
    # else:
    #     for i in range(len(ne)-1):
    #         res*=ne[i]

    # for i,num in enumerate(arr):
    #     if num>0:
    #         res*=num 
    # return res
    mod=10**9+7
    neg=[]
    prod=1
    zero_count=0
    for num in arr:
        if num==0:
            zero_count+=1
        else:
            prod*=num
        
        if num<0:
            neg.append(num)
    
    if zero_count==len(arr):
        return 0
    
    # one negative and rest zeroes
    if len(neg)==1 and zero_count+len(neg)==len(arr):
        return 0
    
    # if neg count is odd, remove the element closest to 0
    if len(neg)%2==1:
        prod=prod//max(neg)
    return prod%mod

def another(arr):
    mx=float('-inf')
    n=len(arr)
    mod=1e9+7
    left,right=1,1

    for i in range(len(arr)):
        if left==0:
            left=1
        if right==0:
            right=1
        
        left*=arr[i]
        right*=arr[n-i-1]

        mx=max(mx,left,right)
    return mx


def another1(arr):
    


# print(findMaxProduct(arr))
# print(findMaxProduct(arr1))
print(another(arr))
print(another(arr1))