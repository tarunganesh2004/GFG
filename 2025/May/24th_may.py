# Sum of all substrings of a number

s="6759"

def sum_of_substrings(s):
    n = len(s)
    total_sum = 0
    factor = 1

    for i in range(n - 1, -1, -1):
        digit = int(s[i])
        total_sum += digit * factor * (i + 1)
        factor = factor * 10 + 1

    return total_sum

print(sum_of_substrings(s))