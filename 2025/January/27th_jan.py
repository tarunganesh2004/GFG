# LRU Cache

# class LRUCache:
#     def __init__(self,cap):
#         self.cap=cap
#         self.cache={}
#         self.queue=[]

#     def get(self,key):
#         if key in self.cache: # if key is present in cache
#             self.queue.remove(key) # remove key from queue
#             self.queue.append(key) # append key to queue
#             return self.cache[key] # return value of key
#         return -1
    
#     def put(self,key,value):
#         if key in self.cache:
#             self.queue.remove(key)
#         elif len(self.cache)==self.cap:
#             del self.cache[self.queue.pop(0)]
#         self.cache[key]=value
#         self.queue.append(key)

# cap=2
# cache=LRUCache(cap)
# Queries=[("put",1,2),("put",2,3),("get",1),("put",3,4),("get",2),("put",4,5),("get",1),("get",3),("get",4)]
# for query in Queries:
#     if query[0]=="put":
#         cache.put(query[1],query[2])
#     elif query[0]=="get":
#         print(cache.get(query[1]),end=" ")

# Another approach to implement LRU cache is using double linkedist+map

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,cap):
        self.cap=cap
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail # type: ignore # tyle: ignore
        self.tail.prev=self.head # type: ignore

    def _remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def _add(self,node):
        temp=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=temp
        temp.prev=node # type: ignore

    def get(self,key):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache)>=self.cap:
                lru_node=self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key] # type: ignore
            new_node=Node(key,value)
            self.cache[key]=new_node
            self._add(new_node)

cap=2
cache=LRUCache(cap)
Queries=[("put",1,2),("put",2,3),("get",1),("put",3,4),("get",2),("put",4,5),("get",1),("get",3),("get",4)]
for query in Queries:
    if query[0]=="put":
        cache.put(query[1],query[2])
    elif query[0]=="get":
        print(cache.get(query[1]),end=" ") # type: ignore