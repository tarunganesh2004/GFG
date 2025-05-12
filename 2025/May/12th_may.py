# Meeting Rooms III


n=2
meetings=[[0,6],[2,3],[3,7],[4,8],[6,8]]


def mostBooked(n,meetings):
    from heapq import heappush, heappop
    from collections import Counter

    rooms=list(range(n))
    used=[]
    counter=Counter()

    for start,end in sorted(meetings):
        while used and used[0][0]<=start:
            _,r=heappop(used)
            heappush(rooms,r)
        if rooms:
            r=heappop(rooms)
            heappush(used,(end,r))
        else:
            t,r=heappop(used)
            heappush(used,(t+end-start,r))
        counter[r]+=1

    return counter.most_common(1).pop()[0]

print(mostBooked(n,meetings))