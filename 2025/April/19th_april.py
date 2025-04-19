# Maximum XOR of Two Numbers

arr=[25,10,2,8,5,3]

# brute force
def brute_force(arr):
    max_xor=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            max_xor=max(max_xor,arr[i]^arr[j])
    return max_xor

# optimized approach is to use Trie 
# create a trie with binary representation of numbers(0,1)

class TrieNode:
    def __init__(self):
        self.children={} # to hold '0' and '1'

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,num):
        node=self.root
        # traverse from lmsb to msb
        for i in range(31,-1,-1):
            bit=(num>>i)&1 # get the ith bit of num
            if bit not in node.children:
                node.children[bit]=TrieNode()
            node=node.children[bit]

class Solution:
    def maxXor(self,arr):
        # create a trie and insert all numbers in it
        trie=Trie()
        for num in arr:
            trie.insert(num)
        
        max_xor=0
        def find_max_xor(num):
            node=trie.root
            xor_num=0
            # traverse from lmsb to msb
            for i in range(31,-1,-1):
                bit=(num>>i)&1
                # check if opposite bit exists in trie
                if 1-bit in node.children:
                    xor_num|=(1<<i)
                    node=node.children[1-bit]
                else:
                    node=node.children[bit]
            return xor_num
        
        for num in arr:
            max_xor=max(max_xor,find_max_xor(num))
        
        return max_xor

print(brute_force(arr))  # Output: 28 (25^5=28)

print(Solution().maxXor(arr))  # Output: 28 (25^5=28)