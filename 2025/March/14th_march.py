# Coin Change(count Ways)

coins=[1,2,5]
amount=5

# recursion 
def bruteForce(coins,n,amount):
    if amount==0:
        return 1
    if amount<0 or n==0:
        return 0 # no way to make change
    
    # include the current coin(n-1) and reduce amount
    include=bruteForce(coins,n,amount-coins[n-1])
    # exclude the current coin(n-1) and keep the amount same
    exclude=bruteForce(coins,n-1,amount)
    return include+exclude

# Recursion another way(without n)
def anotherWay(coins,amount,index=0):
    if amount==0:
        return 1
    if amount<0:
        return 0
    
    total_ways=0
    for i in range(index,len(coins)):
        total_ways+=anotherWay(coins,amount-coins[i],i)
    return total_ways


# Memoization - Top Down
def countWaysMemo(coins,n,amount,memo={}):
    if amount==0:
        return 1
    if amount<0 or n==0:
        return 0
    
    if (n,amount) in memo:
        return memo[(n,amount)]
    
    include=countWaysMemo(coins,n,amount-coins[n-1],memo)
    exclude=countWaysMemo(coins,n-1,amount,memo)
    memo[(n,amount)]=include+exclude
    return memo[(n,amount)]



print(bruteForce(coins,len(coins),amount)) # 4
print(anotherWay(coins,amount)) # 4
print(countWaysMemo(coins,len(coins),amount)) # 4