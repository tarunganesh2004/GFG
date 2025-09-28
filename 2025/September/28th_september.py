# Longest Bounded-Difference Subarray

arr=[8,4,5,6,7]
x=3

def longestSubarray(arr,x):
    n=len(arr)
    best_len=0
    best_start=0
    for i in range(n):
        for j in range(i,n):
            sub_max=max(arr[i:j+1])
            sub_min=min(arr[i:j+1])

            if sub_max-sub_min<=x:
                cur_len=j-i+1
                if cur_len>best_len:
                    best_len=cur_len
                    best_start=i
            else:
                break
    return arr[best_start:best_start+best_len]

# optimized
def optimized(arr,x):
    from heapq import heappop,heappush
    mini=[]
    maxi=[]
    i=0
    ans=[0,0]
    n=len(arr)
    for j in range(n):
        heappush(mini,(arr[j],j))
        heappush(maxi,(-arr[j],j))

        while mini and maxi and abs(mini[0][0]+maxi[0][0])>x:
            if mini[0][1]<maxi[0][1]:
                i=mini[0][1]+1
            else:
                i=maxi[0][1]+1
            while mini and mini[0][1]<i:
                heappop(mini)
            while maxi and maxi[0][1]<i:
                heappop(maxi)
        if abs(mini[0][0]+maxi[0][0])<=x:
            if ans[0]<j-i+1:
                ans=[j-i+1,i]
    return arr[ans[1]:ans[1]+ans[0]]

print(longestSubarray(arr,x))
print(optimized(arr,x))