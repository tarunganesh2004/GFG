# Clone List with next and random pointer(https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.random=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head # type: ignore # type: ignore
        self.head=new_node

    def print_list(self):
        temp=self.head
        while temp:
            print(f"Data: {temp.data}, Random: {temp.random.data if temp.random else None}")
            temp=temp.next

    def clone(self,head):
        if not head:
            return None

        node_map = {}

        dummy = Node(-1)
        curr_original = head
        curr_clone = dummy

        while curr_original:
            new_node = Node(curr_original.data)
            curr_clone.next = new_node # type: ignore
            node_map[curr_original] = new_node
            curr_original = curr_original.next
            curr_clone = curr_clone.next # type: ignore

        curr_original = head
        curr_clone = dummy.next
        while curr_original:
            if curr_original.random:
                curr_clone.random = node_map[curr_original.random] # type: ignore
            curr_original = curr_original.next
            curr_clone = curr_clone.next # type: ignore

        return dummy.next
    
    
ll=LinkedList()
arr=[[1,3],[2,1],[3,5],[4,3],[5,2]]
for i in arr:
    ll.push(i[0])
ll.head.random=ll.head.next.next # type: ignore
ll.head.next.random=ll.head # type: ignore
ll.head.next.next.random=ll.head.next.next.next.next # type: ignore
ll.head.next.next.next.random=ll.head.next.next # type: ignore
ll.head.next.next.next.next.random=ll.head.next # type: ignore
ll.print_list()
print("Cloning...")
new_head=ll.clone(ll.head) # type: ignore
ll.head=new_head
ll.print_list()