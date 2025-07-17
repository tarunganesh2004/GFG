# Power of K in factorial of N 

n=7
k=2

def maxPowerBrute(n,k):
    def computeFactorial(n):
        f=1
        for i in range(1,n+1):
            f *= i
        return f
    
    fact= computeFactorial(n)
    power=0
    while fact%k==0:
        power+=1
        fact //= k
    return power

def optimized(n,k):
    # using Legendre's formula to find the power of k in n!
    # 1st step is to find the prime factorization of k
    def primeFactorization(k):
        i=2
        factors={}
        while i*i<=k:
            count=0
            while k%i==0:
                count+=1
                k//=i
            if count:
                factors[i] = count
            i+=1
        if k>1:
            factors[k] = 1
        return factors
    
    factors = primeFactorization(k)
    min_power= float('inf')
    for prime,exponent in factors.items():
        power=0
        nn=n 
        while nn>0:
            power+= nn // prime
            nn //= prime
        min_power = min(min_power, power // exponent)
    return min_power

print(maxPowerBrute(n,k))
print(optimized(n,k))  # Output: 4