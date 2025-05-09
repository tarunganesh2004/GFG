# Largest Number in K Swaps

s="1234567"
k=4

# Approach: Brute force approach
def largestNumber(s,k):
    if k == 0:
        return s
    
    max_num = s
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            swapped=list(s)
            # print(swapped)
            # print(i,j,swapped[i],swapped[j])
            swapped[i],swapped[j]=swapped[j],swapped[i]
            swapped = ''.join(swapped)
            # print(swapped)
            if swapped > max_num:
                max_num = swapped
            max_num = max(max_num, largestNumber(swapped, k-1))

    
    return max_num

# optimal approach
def largestNumberOptimal(s,k):
    def swap(s,i,j):
        s=list(s)
        s[i],s[j]=s[j],s[i]
        return ''.join(s)

    res=s
    def setDigit(s,idx,res,k):
        if k==0 or idx==len(s)-1:
            res=max(res,s)
            return res
        
        maxdigit=0
        for i in range(idx,len(s)):
            maxdigit=max(maxdigit,int(s[i]))

        if int(s[idx])==maxdigit:
            res=setDigit(s,idx+1,res,k)
            return res
        
        # swap the digit with the max digit
        for i in range(idx+1,len(s)):
            if int(s[i])==maxdigit:
                # swap 
                s=swap(s,idx,i)
                res=setDigit(s,idx+1,res,k-1)
                # backtrack
                s=swap(s,idx,i)
        return res


    res=setDigit(s,0,res,k)
    return res

print(largestNumber(s, k))  # Output: 7654321
print(largestNumberOptimal(s, k))  # Output: 7654321