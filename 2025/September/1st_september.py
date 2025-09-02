# Sum of Mode

arr=[1,2,3,2,5,2,4,4]
k=3

def sumOfModes(arr,k):
    # sliding window
    n=len(arr)
    sum=0

    # iterate over subarrays of size k
    for i in range(n-k+1):

        freq={}
        mode=float('inf')
        maxFreq=0

        for j in range(i,i+k):
            val=arr[j]
            freq[val]=freq.get(val,0)+1

            if freq[val]>maxFreq or (freq[val]==maxFreq and val<mode):
                maxFreq=freq[val]
                mode=val
        sum+=mode
    return sum

print(sumOfModes(arr,k))