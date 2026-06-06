# Non Attacking Black and White Knights

n=2
m=2

def numOfWaysBrute(n,m):
    # n*m 
    moves=[
        (-2,-1),(-2,1),(-1,-2),(-1,2),
        (1,-2),(1,2),(2,-1),(2,1)
    ]

    def attack(r1,c1,r2,c2):
        dr=abs(r1-r2)
        dc=abs(c1-c2)

        return (dr==2 and dc==1) or (dr==1 and dc==2)
    
    ans=0
    for br in range(n):
        for bc in range(m):

            for wr in range(n):
                for wc in range(n):
                    if br==wr and bc==wc:
                        continue # same square

                    if attack(br,bc,wr,wc):
                        continue # attacking is not allowed

                    ans+=1
    return ans 

# now to optimize this
# cells = n*m
# total placements= cells *(cells-1)
# total placements- attacking placements
def optimized(n,m):
    cells=n*m 
    total=cells*(cells-1)
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    attacking=0
    for r in range(n):
        for c in range(m):
            for dr,dc in moves:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    attacking+=1

    return total-attacking

print(numOfWaysBrute(n,m))
print(optimized(n,m))