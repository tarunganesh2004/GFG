# Police and Theives

arr=["T","T","P","P","T","P"]
k=2

def catchTheives(arr,k):
    n=len(arr)
    count=0
    police=0
    theif=0
    while police<n and arr[police]!="P":
        police+=1
    while  theif<n and arr[theif]!="T" :
        theif+=1

    while police<n and theif<n:
        if abs(police-theif)<=k:
            count+=1
            police+=1
            theif+=1
        elif police<n and theif<police:
            theif+=1
        elif theif<n and police<theif:
            police+=1
        
        while  police<n and arr[police]!="P":
            police+=1
        while  theif<n and arr[theif]!="T" :
            theif+=1
    return count

print(catchTheives(arr,k))  # Output: 3