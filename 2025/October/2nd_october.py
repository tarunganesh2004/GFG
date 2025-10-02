# Unique K Number Sum 

n=9
k=3

def uniqueKSum(n,k):
    res=[]
    s=set()
    def dfs(cur,start,target):
        if target==0 and len(cur)==k:
            res.append(cur)
            return
        if target<0 or len(cur)>k:
            return
        for i in range(start,10):
            if i not in s:
                s.add(i)
                dfs(cur+[i],i+1,target-i)
                s.remove(i)
    dfs([],1,n)

    return res

print(uniqueKSum(n,k))
