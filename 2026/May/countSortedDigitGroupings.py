s="1119"

from functools import lru_cache
def validGroups(s):

    n=len(s)
    
    @lru_cache(None)
    def dfs(idx,prev_sum):
        if idx==n:
            return 1
        
        ans=0
        cur_sum=0

        for i in range(idx,n):
            cur_sum+=int(s[i])

            if cur_sum>=prev_sum:
                ans+=dfs(i+1,cur_sum)
        return ans 
    
    return dfs(0,0)

print(validGroups(s))