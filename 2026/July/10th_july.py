# Ways to express as sum of consecutive

n=10
# 1+2+3+4
# n=15, 3 ways (1+2+3+4+5, 4+5+6, 7+8)

"""
n= a+(a+1)+(a+2)........+(a+k-1), k>=2,a=starting number, k(no of consecutive numbers)
"""

# brute force is checking every starting point and length
def bruteForce(n):
    count=0
    for start in range(1,n):
        sum=0
        for x in range(start,n):
            sum+=x 
            if sum==n:
                count+=1
            if sum>n:
                break 
    return count

# optimized
"""
start=a, length=k(no of consecutive numbers we take )
sum=k/2*(first+last), last term a+k-1
sum=k(2a+k-1)/2 =n 
==> 2n=k(2a+k-1)
==> a=(2n/k-k+1)/2

so instead of guessing start we guess length

possible lengths, min sum of k numbers <=n ==> k(k+1)/2<=n 
==> k<=sqrt(2n)
"""
def countWays(n):
    import math 
    ans=0
    # k (length) can only go up to √(2n) because even the smallest length-k sequence is 1+2+...+k.
    for k in range(2,int(math.sqrt(2*n))+1):
        if (2*n)%k==0: # if 2n/k is not an integer , then a cant be an integer
            x=(2*n)//k - k +1 # instead of 2a=2n/k-k+1
            # here 2a=x
            if x>0 and x%2==0: 
                ans+=1
    return ans 

print(bruteForce(n))
print(countWays(n))
