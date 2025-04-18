# # Implement Trie 

# Type 1 : (1, word), calls insert(word) function and insert word in the Trie
# Type 2 : (2, word), calls search(word) function and check whether word exists in Trie or not.
# Type 3 : (3, word), calls isPrefix(word) function and check whether word exists as a prefix of any string in Trie or not.

query=[[1,"abcd"],[1,"abc"],[1,"bcd"],[2,"bc"],[3,"bc"],[2,"abc"]]

class Trie:
    def __init__(self):
        self.children={}
        self.isEnd=False
    
    def insert(self,word):
        node=self
        for char in word:
            if char not in node.children:
                node.children[char]=Trie()
            node=node.children[char]
        node.isEnd=True
    
    def search(self,word):
        node=self
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.isEnd
    
    def isPrefix(self,word):
        node=self
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
    

trie=Trie()
output=[]
for q in query:
    if q[0]==1:
        trie.insert(q[1])
    elif q[0]==2:
        output.append(trie.search(q[1]))
    else:
        output.append(trie.isPrefix(q[1]))
    
print(output)  # Output: [False, True, True]