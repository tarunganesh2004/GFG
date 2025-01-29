# Implement Pow

# Implement the function power(b, e), which calculates b raised to the power of e (i.e. b^e)

b=3.00000
e=5

def power(b,e):
    if e==0:
        return 1
    if e<0:
        return 1/power(b,-e)
    if e%2==0:
        return power(b*b,e//2)
    return b*power(b,e-1)

# O(logn) approach
def pow(b,e):
    n=-e if e<0 else e
    x=b
    ans=1.0
    while n:
        if n&1:
            ans*=x
            n-=1
        else:
            x*=x
            n=n>>1

    if e<0:
        ans=1.0/ans
    return ans

print(power(b,e)) 
print(pow(b,e))