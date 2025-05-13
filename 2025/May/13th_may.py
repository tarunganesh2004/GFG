# nCr

n=5
r=2

def nCr(n,r):
    if r>n:
        return 0
    if r==0 or r==n:
        return 1
    if r==1:
        return n
    if r>n//2:
        r=n-r
    res=1
    for i in range(r):
        res=res*(n-i)//(i+1)
    return res

# Other way O(n) and O(1)
def nCr2(n,r):
    if r>n:
        return 0
    def f(n):
        if n==0:
            return 1
        return n*f(n-1)
    return f(n)//(f(r)*f(n-r))

print(nCr(n,r))
print(nCr2(n,r))