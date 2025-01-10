# Count distinct elements in every window

arr=[1,2,1,3,4,2,3]
k=4

def bruteForce(arr,k): # O(n*k)
    n=len(arr)
    res=[]
    for i in range(n-k+1):
        res.append(len(set(arr[i:i+k])))

    return res

# using sliding window and a map to store the count of elements O(n) & O(n)
def countDistinct(arr,k):
    freq_map={}
    res=[]
    # count the frequency of elements in first window
    for i in range(k):
        if arr[i] in freq_map:
            freq_map[arr[i]]+=1
        else:
            freq_map[arr[i]]=1
    res.append(len(freq_map))

    for i in range(k,len(arr)):
        # remove the first element of previous window i-k
        outgoing=arr[i-k]
        freq_map[outgoing]-=1 # decrease the count of outgoing element
        if freq_map[outgoing]==0:
            del freq_map[outgoing] # remove the element from map

        # add the new element
        ingoing=arr[i]
        if ingoing in freq_map:
            freq_map[ingoing]+=1
        else:
            freq_map[ingoing]=1
        res.append(len(freq_map))

    return res

print(bruteForce(arr,k)) # [3,4,4,3]
print(countDistinct(arr,k)) # [3,4,4,3]