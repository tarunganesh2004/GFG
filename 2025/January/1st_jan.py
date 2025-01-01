# print Anagrams together

from collections import defaultdict


arr=["act","god","cat","dog","tac"]

# Method 1
# using Hashing

def groupAnagrams(arr):
    map={}
    for word in arr:
        key=''.join(sorted(word))
        if key in map:
            map[key].append(word)
        else:
            map[key]=[word]
    return list(map.values())


# Another method
def groupAnagramsAnother(arr): # O(n*k) where n is the number of strings and k is the length of the string
    store=defaultdict(list)
    for string in arr:
        char_count=[0]*26
        for char in string:
            char_count[ord(char)-ord('a')]+=1
        hash_str=''.join(map(str,char_count))
        store[hash_str].append(string)
    return list(store.values())

print(groupAnagrams(arr))
print(groupAnagramsAnother(arr))