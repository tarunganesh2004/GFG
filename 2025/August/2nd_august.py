# Longest Subarray with Majority Greater than K

arr=[1,2,3,4,1]
k=2

# brute force
def bruteForce(arr,k): # O(n^2)
    n=len(arr)
    res=0
    for i in range(n):
        cnt=0
        for j in range(i,n):
            if arr[j] > k:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt > 0:
                res = max(res, j - i + 1)

    return res

# optimized is to use prefix sum(HashMap)
def longestSubarray(arr,k): # O(n)
    n=len(arr)
    map={}
    prefix_sum=0
    res=0
    for i in range(n):
        if arr[i]<=k:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        # if sum is positive then prefix is valid
        if prefix_sum>0:
            res=i+1
        else:
            # check if we have seen this prefix sum before
            if prefix_sum-1 in map:
                res=max(res, i-map[prefix_sum-1])
        
        # store the first occurrence of the prefix sum
        if prefix_sum not in map:
            map[prefix_sum] = i
    return res

print(bruteForce(arr,k))
print(longestSubarray(arr,k))

"""
Java Snippet:
public static int longestSubarray(int[] arr, int k) {
        int n = arr.length;
        int prefixSum = 0;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (arr[i] <= k) {
                prefixSum -= 1;
            } else {
                prefixSum += 1;
            }

            if (prefixSum > 0) {
                res = i + 1;
            } else {
                if (map.containsKey(prefixSum - 1)) {
                    res = Math.max(res, i - map.get(prefixSum - 1));
                }
            }

            if (!map.containsKey(prefixSum)) {
                map.put(prefixSum, i);
            }
        }
        return res;
    }
"""