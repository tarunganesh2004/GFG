# N - Digit Numbers with increasing digits

n=1
n1=2

def increasingNumbers(n):
    ans=[]
    if n==1:
        return [i for i in range(10)]
    
    def backtrack(n,last_digit,num,length,ans):
        if length==n:
            ans.append(num)
            return 
        
        for digit in range(last_digit+1,10):
            backtrack(n,digit,num*10+digit,length+1,ans)
    for start in range(1,10):
        backtrack(n,start,start,1,ans)

    return ans 

print(increasingNumbers(n1))