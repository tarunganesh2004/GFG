# Boolean Parenthesization Problem

s='T|T&F^T'

# brute force
def brute_force(s):
    def recur(s,i,j,isTrue):
        if i>j:
            return False
        
        if i==j:
            if isTrue:
                return s[i]=="T"
            else:
                return s[i]=="F"
        
        ans=0
        for k in range(i+1,j,2):
            lt= recur(s,i,k-1,True)
            lf= recur(s,i,k-1,False)
            rt= recur(s,k+1,j,True)
            rf= recur(s,k+1,j,False)
            
            if s[k]=="&":
                if isTrue:
                    ans+=lt*rt
                else:
                    ans+=lt*rf+lf*rt+lf*rf
            elif s[k]=="|":
                if isTrue:
                    ans+=lt*rt+lt*rf+lf*rt
                else:
                    ans+=lf*rf
            elif s[k]=="^":
                if isTrue:
                    ans+=lt*rf+lf*rt
                else:
                    ans+=lt*rt+lf*rf
        
        return ans
    
    return recur(s,0,len(s)-1,True)

# using lru_cache
def memoi_brute_force(s):
    from functools import lru_cache
    @lru_cache(None)
    def recur(i,j,isTrue):
        if i>j:
            return False
        
        if i==j:
            if isTrue:
                return s[i]=="T"
            else:
                return s[i]=="F"
        
        ans=0
        for k in range(i+1,j,2):
            lt= recur(i,k-1,True)
            lf= recur(i,k-1,False)
            rt= recur(k+1,j,True)
            rf= recur(k+1,j,False)
            
            if s[k]=="&":
                if isTrue:
                    ans+=lt*rt
                else:
                    ans+=lt*rf+lf*rt+lf*rf
            elif s[k]=="|":
                if isTrue:
                    ans+=lt*rt+lt*rf+lf*rt
                else:
                    ans+=lf*rf
            elif s[k]=="^":
                if isTrue:
                    ans+=lt*rf+lf*rt
                else:
                    ans+=lt*rt+lf*rf
        
        return ans
    
    return recur(0,len(s)-1,True)

# Memoization
def memoization(s):
    def recurMemo(i,j,isTrue,memo):
        if i>j:
            return False
        
        if i==j:
            if isTrue:
                return s[i]=="T"
            else:
                return s[i]=="F"
        
        if (i,j,isTrue) in memo:
            return memo[(i,j,isTrue)]
        
        ans=0
        for k in range(i+1,j,2):
            lt= recurMemo(i,k-1,True,memo)
            lf= recurMemo(i,k-1,False,memo)
            rt= recurMemo(k+1,j,True,memo)
            rf= recurMemo(k+1,j,False,memo)
            
            if s[k]=="&":
                if isTrue:
                    ans+=lt*rt
                else:
                    ans+=lt*rf+lf*rt+lf*rf
            elif s[k]=="|":
                if isTrue:
                    ans+=lt*rt+lt*rf+lf*rt
                else:
                    ans+=lf*rf
            elif s[k]=="^":
                if isTrue:
                    ans+=lt*rf+lf*rt
                else:
                    ans+=lt*rt+lf*rf
        
        memo[(i,j,isTrue)]=ans
        return ans
    
    return recurMemo(0,len(s)-1,True,{})

# dp
def dp(s):
    n=len(s)
    dpT=[[0]*n for _ in range(n)]
    dpF=[[0]*n for _ in range(n)]
    for i in range(n):
        if s[i]=="T":
            dpT[i][i]=1
        else:
            dpF[i][i]=1
    
    for l in range(3,n+1):  # noqa: E741
        for i in range(n-l+1):
            j=i+l-1
            for k in range(i+1,j,2):
                lt=dpT[i][k-1]
                lf=dpF[i][k-1]
                rt=dpT[k+1][j]
                rf=dpF[k+1][j]
                
                if s[k]=="&":
                    dpT[i][j]+=lt*rt
                    dpF[i][j]+=lt*rf+lf*rt+lf*rf
                elif s[k]=="|":
                    dpT[i][j]+=lt*rt+lt*rf+lf*rt
                    dpF[i][j]+=lf*rf
                elif s[k]=="^":
                    dpT[i][j]+=lt*rf+lf*rt
                    dpF[i][j]+=lt*rt+lf*rf
    
    return dpT[0][n-1]

print(brute_force(s)) # 4
print(memoi_brute_force(s)) # 4
print(memoization(s)) # 4
print(dp(s)) # 4