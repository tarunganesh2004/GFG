# Majority Element More than n/3 times

arr=[2,2,3,1,3,2,1,1]

# using map 
def bruteForce(arr):
    from collections import Counter 
    freq=Counter(arr)
    for key,value in freq.items():
        if value > len(arr)//3:
            return key
    return -1

# using Boyer-Moore Voting Algorithm
def boyerMoore(arr):
    count1, count2, candidate1, candidate2 = 0, 0, None, None

    for num in arr:
        if candidate1 is not None and num == candidate1:
            count1 += 1
        elif candidate2 is not None and num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Verify candidates
    count1, count2 = 0, 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(arr) // 3:
        result.append(candidate1)
    if count2 > len(arr) // 3:
        result.append(candidate2)

    return result if result else -1
print(bruteForce(arr))
print(boyerMoore(arr))