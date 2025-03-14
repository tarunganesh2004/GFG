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


    

print(bruteForce(coins,len(coins),amount)) # 4