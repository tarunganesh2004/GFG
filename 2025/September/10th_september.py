# Largest Number in one Swap 

s="768"

def largestSwap(s):
    arr=sorted(s,key=lambda e:-ord(e))
    i=0
    while i<len(s):
        if s[i]<arr[i]:
            break
        i+=1
    else:
        return s
    j=s.rfind(arr[i])
    arr=list(s)
    arr[i],arr[j]=arr[j],arr[i]
    return ''.join(arr)

print(largestSwap(s))