# Maximum Sum Path in Two Arrays 

a=[2,3,7,10,12]
b=[1,5,7,8]

def maxPathSum(a,b):
    # keep two running sums,
    # near the common element in both arrays, sum1 & sum2
    # one segment in A, one segment in B, then take the larger segment, before and after the common element 
    n=len(a)
    m=len(b)
    i=j=0
    sum1=0
    sum2=0
    ans=0

    while i<n and j<m:
        if a[i]<b[j]:
            sum1+=a[i]
            i+=1
        elif a[i]>b[j]:
            sum2+=b[j]
            j+=1
        else:
            # common element
            ans+=max(sum1,sum2)
            ans+=a[i] # add the common element

            sum1=0 # now reset, bcz we got a left segment path, now we need right segment            
            sum2=0

            i+=1
            j+=1
    
    while i<n:
        sum1+=a[i]
        i+=1
    
    while j<m:
        sum2+=b[j]
        j+=1
    
    ans+=max(sum1,sum2)

    return ans # O(n+m)

print(maxPathSum(a,b))