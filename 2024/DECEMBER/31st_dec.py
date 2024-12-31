# Longest Consecutive Sequence
from sortedcontainers import SortedSet
arr = [2, 6, 1, 9, 4, 5, 3]

# approach one is to sort the array and then find the longest consecutive sequence
# O(nlogn) & O(1)

def longestConsecutive(arr):
    # arr.sort() 
    # here instead of using .sort we can use SortedSet from sortedcontainers module
    arr=list(SortedSet(arr)) # TC O(nlogn) & SC O(n)
    c=1
    longest=1

    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            c+=1
        # elif arr[i]==arr[i-1]: # if there are duplicates
        #     continue if we use SortedSet no need to check for duplicates
        else:
            longest = max(longest, c)
            c=1
    return longest

# approach two is to use a set to store the elements and then find the longest consecutive sequence
# O(n) & O(n)
def longestConsecutiveSequence(arr):
    s=set(arr)
    longest=0
    for num in s:
        if num-1 not in s: # sequence starts from here
            cur_num=num
            cur_len=1 

            while cur_num+1 in s:
                cur_num+=1
                cur_len+=1

            longest = max(longest, cur_len)
    return longest

print(longestConsecutiveSequence(arr))

print(longestConsecutive(arr))