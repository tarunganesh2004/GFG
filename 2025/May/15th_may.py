# substrings with same first and last characters

s="abcab"
def count_substrings(s):
    from collections import Counter
    n = len(s)
    count = 0
    freq= Counter(s)
    for i in freq:
        count += (freq[i] * (freq[i] - 1)) // 2
    count += n

    return count

print(count_substrings(s))