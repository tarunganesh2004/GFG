# Design Min Max Queue

# idea is to use two queues for min and max in O(1)

from collections import deque


class SpecialQueue:

    def __init__(self):
        self.queue=deque()
        self.min_deque=deque() # increasing order
        self.max_deque=deque() # decreasing order

    def enqueue(self,val):
        # insert at rear 
        self.queue.append(val)

        # maintain increasing order in min_deque
        while self.min_deque and self.min_deque[-1]>val:
            self.min_deque.pop()
        self.min_deque.append(val)

        # maintain decreasing order in max_deque
        while self.max_deque and self.max_deque[-1]<val:
            self.max_deque.pop()
        self.max_deque.append(val)

    def dequeue(self):
        val=self.queue.popleft()
        if val==self.min_deque[0]:
            self.min_deque.popleft()
        if val==self.max_deque[0]:
            self.max_deque.popleft()

    def getFront(self):
        return self.queue[0]
    
    def getMin(self):
        return self.min_deque[0]
    
    def getMax(self):
        return self.max_deque[0]
    
q=6
sq=SpecialQueue()
queries=[[1,4],[1,2],[3],[4],[2],[5]]
for query in queries:
    if query[0]==1:
        sq.enqueue(query[1])
    elif query[0]==2:
        sq.dequeue()
    elif query[0]==3:
        print(sq.getFront())
    elif query[0]==4:
        print(sq.getMin())
    else:
        print(sq.getMax())

        