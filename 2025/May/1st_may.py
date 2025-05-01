# Pascal Triangle 

n=4

def nthRowOfPascalTriangle(n):
    res=[]
    for i in range(n):
        res.append([1]*(i+1))
        for j in range(1,i):
            res[i][j]=res[i-1][j-1]+res[i-1][j]
    return res[n-1]

# using binomial coefficient
def binomialCoefficient(n):
    res=[]
    c=1 # nC0 = 1
    res.append(c)
    for i in range(1,n+1): # each rowis [nC0, nC1, nC2, ... nCn]
        # so here we needto find nCi, (by using formula nCr=nC(r-1)*(n-r+1)/r) 
        c=c*(n-i+1)//i # nCi = nC(i-1)*(n-i+1)/i
        res.append(c)
    return res

# printing entire pascal triangle
def printPascalTriangle(n):
    for i in range(n):
        print(binomialCoefficient(i))
    

print(nthRowOfPascalTriangle(n))
print(binomialCoefficient(n))
printPascalTriangle(n)