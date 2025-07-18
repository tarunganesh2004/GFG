# LCM Triplet

n=9

# brute force
def bruteForce(n):
    def lcm(a,b):
        import math 
        return (a * b) // math.gcd(a, b)
    
    max_lcm=0
    # iterate over all triplets 
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                current_lcm = lcm(lcm(i, j), k)
                max_lcm = max(max_lcm, current_lcm)
    return max_lcm

# optimized O(1)
def optimized(n):
    # if n is odd, triplet is (n, n-1, n-2) is coprime
    # so answer is lcm(n, n-1, n-2)

    # if n is even, (n,n-1,n-3) is better (because n and n-2 both are even share factor 2)

    def lcm(a,b):
        import math 
        return (a * b) // math.gcd(a, b)
    def lcm3(a, b, c):
        return lcm(lcm(a, b), c)
    
    if n<=2:
        return n
    if n==3:
        return 6
    if n % 2 == 1:  # n is odd
        return lcm3(n, n - 1, n - 2)
    else:
        # two possible triplets (n, n-1, n-3) and (n-1, n-2, n-3)
        return max(lcm3(n, n - 1, n - 3), lcm3(n - 1, n - 2, n - 3))

print(bruteForce(n))  # Output: 504
print(optimized(n))  # Output: 504