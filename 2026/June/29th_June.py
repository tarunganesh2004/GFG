# Maximum Dot product with 0 insertions

a=[2,3,1,7,8]
b=[3,6,7]

# brute force trying all combinations 
# this approach is waste doesnt work at all(only works for less values of m&n)
def bruteForce(a,b):
    # from itertools import combinations
    m=len(a)
    n=len(b)

    zeroes_to_insert=m-n 
    if zeroes_to_insert<0:
        return None 

    max_dot=float('-inf')

    # instead of combinations we can separately generate those
    def generate_positions(m,n,start=0,current=None,result=None):
        if current is None:
            current=[]
        if result is None:
            result=[]
        
        if len(current)==n:
            result.append(current[:])
            return 
        
        # try each possible position from start
        for pos in range(start,m):
            current.append(pos) # choose this position
            generate_positions(m,n,pos+1,current,result) # next postion
            current.pop() # backtrack
        return result
    
    all_positions=generate_positions(m,n)

    # Generate all possible positions where a2's elements can go
    # Example: if m=3, n=2 → positions could be (0,1), (0,2), (1,2)
    for positions in all_positions: # type: ignore
        new_b=[0]*m 

        # place b's elements into the choosen positions
        for idx,pos in enumerate(positions):
            new_b[pos]=b[idx]
        
        dot=0
        for i in range(m):
            dot+=(a[i]*new_b[i])
        
        if dot>max_dot:
            max_dot=dot 

    return max_dot

print(bruteForce(a,b))

# recursion
def bruteForceRecursion(a,b):
    m,n=len(a),len(b)

    def solve(i,j):
        if j==n:
            return 0
        if i==m:
            return float('-inf')
        
        # match 
        match=a[i]*b[j]+solve(i+1,j+1)

        # skip 
        skip=solve(i+1,j)

        res=max(match,skip)
        return res
    
    return solve(0,0)

# memoization
def memoization(a,b):
    m,n=len(a),len(b)
    memo={}
    
    def solve(i,j):
        if j==n:
            return 0
        if i==m:
            return float('-inf')
        
        if (i,j) in memo:
            return memo[(i,j)]
        
        match=a[i]*b[j]+solve(i+1,j+1)

        # skip 
        skip=solve(i+1,j)

        memo[(i,j)]=max(match,skip)
        return memo[(i,j)]
    
    return solve(0,0)

def maxDotProduct(a,b):
    if len(a)<len(b):
        a,b=b,a
    
    m,n=len(a),len(b)
    NEG=float('-inf')

    dp=[[NEG]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][n]=0

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            take=(a[i]*b[j]+dp[i+1][j+1])

            skip=dp[i+1][j]

            dp[i][j]=max(take,skip)

    return dp[0][0]

print(bruteForceRecursion(a,b))