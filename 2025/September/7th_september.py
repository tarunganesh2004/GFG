# Merge k sorted Linked lists 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def mergeKLists(self,lists):
        import heapq
        minHeap=[]
        for l in lists:  # noqa: E741
            current=l
            while current:
                heapq.heappush(minHeap,current.data)
                current=current.next 
        dummy=Node(0)
        current=dummy 
        while minHeap:
            val=heapq.heappop(minHeap)
            current.next=Node(val) # type: ignore
            current=current.next  # type: ignore
        return dummy.next