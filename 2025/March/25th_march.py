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

print(brute_force(s)) # 4
print(memoi_brute_force(s)) # 4
print(memoization(s)) # 4