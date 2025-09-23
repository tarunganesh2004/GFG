# Queue Reversal

q=[5,10,15,20,25]

def reverse_queue(q):
    stack=[]
    # dequeue all elements from queue and push them onto stack
    while q:
        stack.append(q.pop(0))
    # pop all elements from stack and enqueue them back to queue
    while stack:
        q.append(stack.pop())
    return q
print(reverse_queue(q))