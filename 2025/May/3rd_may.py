# Prime List
# replace all numbers in the linked list with nearest prime number

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    if n<2:
        return 2
    if is_prime(n):
        return n
    lower = n - 1
    upper = n + 1
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node # type: ignore

    def replace_with_nearest_prime(self):
        current = self.head
        while current:
            current.val = nearest_prime(current.val)
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

arr=[2,6,11]
ll = LinkedList()
for i in arr:
    ll.append(i)
ll.replace_with_nearest_prime()
ll.print_list()