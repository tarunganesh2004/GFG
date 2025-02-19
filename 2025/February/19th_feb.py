# Merge K sorted LinkedLists

# Given a list of sorted linked lists, merge them into a single sorted linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def merge(self,lists):
        import heapq
        heap = []
        for i in lists: # type: ignore
            while i:
                heapq.heappush(heap, i.value)
                i = i.next
        head = Node(0)
        curr = head
        while heap:
            curr.next = Node(heapq.heappop(heap))
            curr = curr.next
        return head.next
    
    def print_list(self):
        temp = self
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

arr=[[1,2,3],[4,5],[5,6],[7,8]]
lists = []
for i in arr:
    head = Node(0)
    temp = head
    for j in i:
        temp.next = Node(j) # type: ignore
        temp = temp.next # type: ignore
    lists.append(head.next)

Node.merge(lists).print_list() # type: ignore
print()