# Course Schedule II 

def findOrder(n,prerequisites):
    from collections import defaultdict

    adj=defaultdict(set)
    idg=defaultdict(int)
    for sto,sta in prerequisites:
        adj[sta].add(sto)
        idg[sto]+=1
    
    res=[]
    q=[x for x in range(n) if idg[x]==0]
    while q:
        node=q.pop(0)
        res.append(node)
        for nei in adj[node]:
            idg[nei]-=1
            if idg[nei]==0:
                q.append(nei)
    return res if len(res)==n else []