# Count the Coprimes 
import math
from collections import Counter

arr=[1,2,3]


# brute force
def bruteForce(arr): # O(n^2 log(max(arr)))
    count=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if math.gcd(arr[i], arr[j]) == 1:
                count += 1
    return count

# better approach using frequency count
def countCoprimes(arr): # O(n^2 log(max(arr)))
    freq = Counter(arr)
    unique=list(freq.keys())
    ans=0

    for i in range(len(unique)):
        a= unique[i]
        # (a,a) pairs
        if math.gcd(a, a) == 1:
            ans += freq[a] * (freq[a] - 1) // 2
        # (a,b) pairs a<b 
        for j in range(i + 1, len(unique)):
            b = unique[j]
            if math.gcd(a, b) == 1:
                ans += freq[a] * freq[b]
    return ans

# optimized approach is to use Mobius function and inclusion-exclusion principle

def countCoprimesOptimized(arr):
    def computeMobius(n,mu):
        is_prime=[1]*(n+1)
        mu[0]=0
        mu[1]=1
        for i in range(2, n + 1):
            if is_prime[i]:
                for j in range(i,n+1,i):
                    mu[j] *= -1
                    is_prime[j]=0
                for j in range(i*i,n+1,i*i):
                    mu[j]=0

    def buildFre(arr,freq):
        for num in arr:
            freq[num] += 1

    def computeDivCount(maxVal,freq,d):
        for k in range(1, maxVal + 1):
            for j in range(k, maxVal + 1, k):
                d[k] += freq[j]

    maxVal= max(arr)

    freq= [0] * (maxVal + 1)
    d= [0] * (maxVal + 1)
    mu= [1] * (maxVal + 1)

    buildFre(arr, freq)
    computeDivCount(maxVal, freq, d)
    computeMobius(maxVal, mu)
    ans = 0

    for k in range(1, maxVal + 1):
        if mu[k]==0 or d[k]<2:
            continue 

        pairs= d[k] * (d[k] - 1) // 2
        ans += mu[k] * pairs
    return ans



print(bruteForce(arr))
print(countCoprimes(arr))
print(countCoprimesOptimized(arr))