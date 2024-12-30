# find triplets with sum 0

arr=[0,-1,2,-3,1]

class Solution:
    def findTriplets(self,arr):
        n = len(arr)
        arr = [(arr[i], i) for i in range(n)]
        arr.sort()
        ans = []
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if arr[i][0] + arr[j][0] + arr[k][0] == 0:
                    ans.append(list(sorted([arr[i][1], arr[j][1], arr[k][1]])))
                    # The other option of considering the j++
                    for u in range(j + 1, k):
                        if arr[i][0] + arr[u][0] + arr[k][0] == 0:
                            ans.append(list(sorted([arr[i][1], arr[u][1], arr[k][1]])))
                    k -= 1
                elif arr[i][0] + arr[j][0] + arr[k][0] > 0:
                    k -= 1
                else:
                    j += 1
        return ans
    
    def anotherApproach(self,arr):
        # using Map
        n=len(arr)
        res=[]
        for i in range(n-2):
            seen={}
            for j in range(i+1,n):
                complement=-(arr[i]+arr[j])
                if complement in seen:
                    res.append(sorted([seen[complement],i,j]))
                
                seen[arr[j]]=j

        return res
sol = Solution()
print(sol.findTriplets(arr))
print(sol.anotherApproach(arr))