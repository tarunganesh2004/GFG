# is LinkedList Even


l=[9,4,3]

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node

        else:
            cur=self.head
            while cur.next:
                cur=cur.next

            cur.next=new_node # type: ignore

    def __str__(self):
        res=""
        cur=self.head

        while cur:
            res+=str(cur.data)+(" -> " if cur.next else "")
            cur=cur.next
        return res
    
    def is_even_length(self):
        c=0
        cur=self.head
        while cur:
            c+=1
            cur=cur.next

        return c%2==0
    
ll=LinkedList()
for k in l:
    ll.add(k)

print(ll)
print(ll.is_even_length())