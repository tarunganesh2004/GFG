# Case Specific Sorting of Strings

s="GEeks"

def caseSort(s):
    # Extract lowercase and uppercase characters
    lower = sorted([c for c in s if c.islower()])
    upper = sorted([c for c in s if c.isupper()])

    # Merge them back into a single string
    result = []
    lower_index, upper_index = 0, 0

    for c in s:
        if c.islower():
            result.append(lower[lower_index])
            lower_index += 1
        else:
            result.append(upper[upper_index])
            upper_index += 1

    return ''.join(result)

print(caseSort(s))  