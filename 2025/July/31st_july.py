# Powerful Integer

n=3
intervals=[[1,3],[4,6],[3,4]]
k=2

def powerfulInteger(n, intervals, k):
    map={}
    for start,end in intervals:
        map[start]=map.get(start,0)+1
        map[end+1]=map.get(end+1,0)-1

    ans=-1
    temp=0

    for point in sorted(map):
        delta=map[point]
        if delta>=0:
            temp+=delta
            if temp>=k:
                ans=point
        else:
            if temp>=k:
                ans=point-1
            temp+=delta
    return ans

print(powerfulInteger(n, intervals, k))  