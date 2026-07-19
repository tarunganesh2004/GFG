# Mountain Subarray queries

arr=[2,3,2,4,4,6,3,2]
queries=[[0,2],[1,3]]

"""
This left-right preprocessing pattern (using inc & dec arrays)
here the optimized idea is
can the increasing part from the left reach the beginning of the decreasing part from the right
we take two arrays incEnd and decStart
incEnd[i] means starting from index i how can I go while the array remains non decreasing
decStart[i] --> for a decreasing sequence ending at i,where can it start

"""

def mountainQueries(arr,queries):
    n=len(arr)

    # inc[i]=farthest index reachable from i 
    # while array is non-decreasing
    inc=[0]*n 
    inc[n-1]=n-1 

    for i in range(n-2,-1,-1):
        if arr[i]<=arr[i+1]:
            inc[i]=inc[i+1]
        else:
            inc[i]=i
    
    # dec[i] = farthest index reachable from i  
    # while array is non-increasing

    dec=[0]*n 
    dec[0]=0
    for i in range(1,n):
        if arr[i-1]>=arr[i]:
            dec[i]=dec[i-1]
        else:
            dec[i]=i
        
    ans=[]
    for l,r in queries:
        peak=inc[l]
        if dec[r]<=peak:
            ans.append(True)
        else:
            ans.append(False)
    return ans 

print(mountainQueries(arr,queries))