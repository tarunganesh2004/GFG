# Generate Binary Numbers

n=4

def generate(n):
    result=[]
    queue=[]
    queue.append("1")

    for i in range(n):
        front=queue.pop(0)
        result.append(front)

        queue.append(front+"0")
        queue.append(front+"1")
    
    return result

def another(n):
    res=[]
    for i in range(1,n+1):
        res.append(bin(i)[2:])
    return res

print(generate(n))