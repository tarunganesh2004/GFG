# Shortest Unique Prefix for Every Word

arr = ["zebra", "dog", "duck", "dove"]

# bruteforce
def bruteForce(arr):
    res=[]
    for word in arr:
        for i in range(1,len(word)+1):
            prefix=word[:i]
            c=0
            for other in arr:
                if other.startswith(prefix):
                    c+=1
            if c==1:
                res.append(prefix)
                break
    return res

# Optimized approach is to use trie, 
# maintain a count variable-> to store how many words passed through each node 
# the ones with count==1 have unique prefic

class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.count=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        cur=self.root 
        for ch in word:
            idx=ord(ch)-ord('a')

            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]

            cur.count+=1

    def get_unique_prefix(self,word):
        cur=self.root
        prefix=""
        for ch in word:
            idx=ord(ch)-ord('a')
            cur=cur.children[idx]

            prefix+=ch 
            if cur.count==1:
                return prefix
        return word 
    
def shortest_unique_prefixes(arr):
    trie=Trie()
    for word in arr:
        trie.insert(word)
    
    res=[]
    for word in arr:
        res.append(trie.get_unique_prefix(word))
    return res 

print(shortest_unique_prefixes(arr))