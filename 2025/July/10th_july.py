# Find the Longest String 

from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie():
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        isValid= True
        cur= self.root
        for i in word[:-1]:
            cur= cur.children[i]
            if not cur.is_end_of_word:
                isValid= False
        cur= cur.children[word[-1]]
        cur.is_end_of_word= True
        return isValid
    
class Solution():
    def longestString(self,arr):
        trie=Trie()
        arr.sort()
        res=""
        for word in arr:
            if trie.insert(word) and len(word) > len(res):
                res = word
        return res
    
s=Solution()
arr = ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
print(s.longestString(arr))  # Output: "pros"