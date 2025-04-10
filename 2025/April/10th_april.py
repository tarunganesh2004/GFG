# Minimum Cost to connect all houses in a city 

n=5
houses=[[0,7],[0,9],[20,7],[30,7],[40,70]]


def minCost(houses):
    dist=lambda i,j: abs(houses[i][0]-houses[j][0])+abs(houses[i][1]-houses[j][1])  # noqa: E731

    if len(houses)==1:
        return 0
    
    edges=[]
    for i in range(len(houses)-1):
        for j in range(i+1,len(houses)):
            edges.append((i,j,dist(i,j)))
    
    edges.sort(key=lambda x:x[2])

    parent=list(range(len(houses)))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    costs=0
    for u,v,cost in edges:
        pu=find(u)
        pv=find(v)
        if pu!=pv:
            costs+=cost
            parent[pu]=pv

    return costs

print(minCost(houses)) # 105

