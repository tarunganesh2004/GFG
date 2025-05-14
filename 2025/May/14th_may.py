# Look and Say Pattern

n=5

def countAndSay(n):
    if n==1:
        return "1"
    
    cur="1"

    for i in range(2,n+1):
        next_seq=""
        count=1
        for j in range(1,len(cur)):
            if cur[j]==cur[j-1]:
                count+=1
            
            else:
                next_seq+=str(count)+cur[j-1]
                count=1
        next_seq+=str(count)+cur[-1]
        cur=next_seq

    return cur


print(countAndSay(n))