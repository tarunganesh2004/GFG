# Insert in Sorted Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # type: ignore
            return

        current = self.head
        prev = None

        while True:
            if current.data >= data: # type: ignore
                break
            prev = current
            current = current.next # type: ignore
            if current == self.head:
                break

        new_node.next = current # type: ignore
        if prev:
            prev.next = new_node # type: ignore
        else:
            # Insert at the head
            new_node.next = self.head # type: ignore
            self.head = new_node

    def display(self):
        if not self.head:
            return "List is empty"
        
        result = []
        current = self.head
        while True:
            result.append(current.data) # type: ignore
            current = current.next # type: ignore
            if current == self.head:
                break
        return " -> ".join(map(str, result))


arr=[1,2,4]
cll = CircularLinkedList()
for value in arr:
    cll.insert_sorted(value)
print(cll.display())
data=2
cll.insert_sorted(data)
print(cll.display())