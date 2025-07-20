# Count Numbers Containing Specific Digits

n=2
arr=[3,5]

# brute force
def bruteForce(n,arr): # O(n * 10^n)
    if n==1:
        return len(arr)
    arr_set=set(str(x) for x in arr)
    count=0

    start=10**(n-1)
    end=10**n
    for i in range(start,end):
        num_str=str(i)
        found=False
        for digit in num_str:
            if digit  in arr_set:
                found=True
                break
        if  found:
            count+=1
    return count

# optimized is to use compliment method
def optimized(n,arr): # O(1)
    total=9*(10**(n-1))  # Total n-digit numbers(10^n - 10^(n-1))

    all_digits=set(range(10)) # Digits from 0 to 9
    arr_set=set(arr)
    bad_digits=all_digits-arr_set # Digits not in arr
    if not bad_digits:
        return total
    
    bad_digits=list(bad_digits)
    if 0 in bad_digits:
        first_digit_choice=len(bad_digits)-1
    else:
        first_digit_choice=len(bad_digits)
    
    if first_digit_choice==0:
        bad_count=0 # No bad digits, all n-digit numbers are valid
    else:
        bad_count=first_digit_choice *(len(bad_digits)**(n-1)) # First digit can be any of the bad digits, rest can be any of the bad digits
    return total-bad_count


print(bruteForce(n,arr))
print(optimized(n,arr))