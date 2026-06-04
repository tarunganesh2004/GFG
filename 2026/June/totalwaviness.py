# LC 3751

num1=120
num2=130

def totalWaviness(num1,num2):
    def findwaviness(num):
        w=0
        s=str(num)
        n=len(s)
        if n<3:
            return 0
        for i in range(1,n-1):
            if s[i]>s[i-1] and s[i]>s[i+1]:
                w+=1
            elif s[i]<s[i-1] and s[i]<s[i+1]:
                w+=1
        return w
            
    c=0
    
    for i in range(num1,num2+1):
        w=findwaviness(i)
        c+=w
    return c