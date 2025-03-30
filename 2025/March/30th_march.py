# Gas Station

gas=[4,5,7,4]
cost=[6,6,3,5]

def startStation(gas,cost):
    gc=[g-c for g,c in zip(gas,cost)]
    start,running,n,cnt=-1,0,len(gc),0

    for i in range(2*n):
        e=gc[i%n]
        running+=e
        if running<0:
            running=0
            start=-1
            cnt=0
        else:
            if start==-1:
                start=i
            cnt+=1
        if cnt==n:
            break
    
    return -1 if cnt!=n else start

print(startStation(gas,cost)) # 2