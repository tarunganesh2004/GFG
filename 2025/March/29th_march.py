# Job Sequencing Problem

import heapq


deadline=[4,1,1,1]
profit=[20,10,40,30]

def jobSequencing(deadline,profit):
    n=len(deadline)
    ans=[0,0]
    jobs=[(deadline[i],profit[i]) for i in range(n)]
    jobs.sort()
    pq=[]
    for job in jobs:
        if job[0]>len(pq):
            heapq.heappush(pq,job[1])
        elif pq and pq[0]<job[1]:
            heapq.heappop(pq)
            heapq.heappush(pq,job[1])

    while pq:
        ans[0]+=1
        ans[1]+=heapq.heappop(pq)
    return ans


print(jobSequencing(deadline,profit)) # 60