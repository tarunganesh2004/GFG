# Divisible by 13

s="2911285"

# brute force
def is_divisible_by_13(s):
    n = int(s)
    return n % 13 == 0

# String based modulo
def optimized(s):
    # process number digit by digit from left to right
    # maintaining the remainder modulo 13

    rem=0
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13
    return rem == 0

print(is_divisible_by_13(s))  # Output: True 
print(optimized(s))  # Output: True