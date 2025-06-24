# Lexicographically Largest String After K Deletions 

s="ritz"
k=2

def maxSubSeq(s,k):
    res=""
    n=len(s)
    to_remove=k 
    for i in range(n):
        while res and to_remove>0 and res[-1]<s[i]:
            res=res[:-1]
            to_remove-=1
        res+=s[i]
    
    return res[n-k]

# another approach using stack
# def anotherApproach(s,k):
#     stack=[]
#     n=len(s)
#     to_remove=n-k 
#     for i in range(n):
#         while stack and stack[-1]<s[i] and k>0:
#             stack.pop()
#             k-=1
#         stack.append(s[i])
    
#     res=""
#     while stack:
#         res+=stack[-1]
#         stack.pop()
    

print(maxSubSeq(s, k))  # Output: "tz"