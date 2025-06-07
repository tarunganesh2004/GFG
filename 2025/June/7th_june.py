# Longest Span in Two Binary Arrays

a1=[0,1,0,0,0,0]
a2=[1,0,1,0,0,1]

def longest_span(a1, a2):
    n = len(a1)
    max_len = 0
    sum_map = {0: -1}  # To handle the case when sum is zero at the start

    sum_a1 = 0
    sum_a2 = 0

    for i in range(n):
        sum_a1 += a1[i]
        sum_a2 += a2[i]

        diff = sum_a1 - sum_a2

        if diff in sum_map:
            max_len = max(max_len, i - sum_map[diff])
        else:
            sum_map[diff] = i

    return max_len

print(longest_span(a1, a2))  # Output: 4