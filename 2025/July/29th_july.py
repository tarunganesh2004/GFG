# ASCII Range Sum 

s="abacab"

def ascii_range_sum(s):
    n = len(s)
    dp=[0]*n 

    acc=0
    for i,e in enumerate(s):
        acc+=ord(e)
        dp[i]=acc

    m={}
    for i in range(n-1,-1,-1):
        e=s[i]
        if e not in m:
            m[e]=i  
    ans=[]
    for i,e in enumerate(s):
        if e in m and m[e]-i>1:
            ans.append(dp[m[e]-1]-dp[i])
            m.pop(e)
    return ans 

print(ascii_range_sum(s))