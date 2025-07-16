# Nine Divisors


n=100

def countNumbersBrute(n):
    def countDivisors(x):
        count=0
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                count += 1
                if i != x // i:
                    count += 1
        return count
    
    count = 0
    for i in range(1, n + 1):
        if countDivisors(i) == 9:
            count += 1
    return count

def countNumbersOptimized(n):
    if n<36:
        return 0
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [i for i in range(limit + 1) if is_prime[i]]

    # part 1 ,primes for p^8<=n 
    def count_p8(n,primes):
        limit_p8 = int(n**(1/8))
        count = 0
        for p in primes:
            if p > limit_p8:
                break
            count += 1
        return count

    # part 2, primes for p^2*q^2<=n

    def count_p2_q2(n,primes):
        root=int(n**0.5)
        count = 0
        for i in range(len(primes)):
            p=primes[i]
            max_q=root//p  # q must satisfy q<= √n / p
            if max_q<= p:
                break

            # loop from i+1 to end and count how many q ≤ max_q
            for j in range(i+1, len(primes)):
                q = primes[j]
                if q > max_q:
                    break
                count += 1
        return count

    root=int(n**0.5)
    primes = sieve(root)
    count = count_p8(n, primes) + count_p2_q2(n, primes)
    return count



print(countNumbersBrute(n))  # Output: 2
print(countNumbersOptimized(n))  # Output: 2