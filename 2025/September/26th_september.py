# Rotate Deque By K

dq=[1,2,3,4,5,6]
type=2
k=2

def rotateDeque(dq,type,k):
    from collections import deque
    n=len(dq)
    k=k%n
    dq=deque(dq)
    if type==1: # clockwise
        dq.rotate(k)
    else: # anticlockwise
        dq.rotate(-k)
    return dq

print(rotateDeque(dq,type,k))