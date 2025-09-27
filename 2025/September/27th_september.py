# Minimum K Consecutive Bit Flips

arr=[1,1,0,0,0,1,1,0,1,1,1]
k=2

# brute force
def kBitFlips(arr,k):
    n=len(arr)
    flipped=0
    is_flipped=[0]*n 
    operations=0

    for i in range(n):
        if i>=k:
            flipped^=is_flipped[i-k]
        if (arr[i]^flipped)==0:
            if i+k>n:
                return -1
            operations+=1
            flipped^=1
            is_flipped[i]=1
    return operations

print(kBitFlips(arr,k))