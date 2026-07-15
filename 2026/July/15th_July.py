# Longest Bitonic Subarray 

arr=[12,4,78,90,45,23]

# brute force is checking every subarray
def bruteForce(arr): # O(n^3)
    ans=1
    def bitonic(arr):
        n=len(arr)
        phase="inc"
        for i in range(1,len(arr)):
            if phase=="inc":
                # still increasing
                if arr[i]>=arr[i-1]:
                    continue
                else:
                    phase="dec" # 1st decrease -> switch phase
            if phase=="dec":
                # must be decreasing
                if arr[i]<=arr[i-1]:
                    continue
                else:
                    return False
                
        return True
        
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if bitonic(arr[i:j]):
                ans=max(ans,j-i)
    return ans 


# optimized approach is using two arrays
# one is increment array(stores length of longest increasing subarray at index i)
# another one is decrement array 
def bitonic(arr):
    n=len(arr)
    inc=[1]*n 

    # for every index if prev<= cur element extend , else start a new chain 
    for i in range(1,n):
        if arr[i]>=arr[i-1]:
            inc[i]=inc[i-1]+1 # no need to write else, bcz we already declared with inc array with 1's 
        
    dec=[1]*n 
    # start from the end 
    for i in range(n-2,-1,-1): # n-2 bcz we need to compare with i+1
        if arr[i]>=arr[i+1]:
            dec[i]=dec[i+1]+1

    ans=1
    for i in range(n):
        ans=max(ans,inc[i]+dec[i]-1)
    return ans 

print(bruteForce(arr))
print(bitonic(arr))