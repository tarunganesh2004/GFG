# Minimum Cost to cut a board into squares

n=4
m=6
x=[2,1,3,1,4]
y=[4,1,2]

def minCost(x,y,n,m):
    hx,vr=1,1
    x.sort(reverse=True)
    y.sort(reverse=True)
    ans,i,j=0,0,0
    r,c=len(x),len(y)
    while i<r and j<c:
        if x[i]>=y[j]:
            ans+=x[i]*vr
            hx+=1
            i+=1
        else:
            ans+=y[j]*hx
            vr+=1
            j+=1
    while i<r:
        ans+=x[i]*vr
        hx+=1
        i+=1

    while j<c:
        ans+=y[j]*hx
        vr+=1
        j+=1
    return ans

print(minCost(x,y,n,m))