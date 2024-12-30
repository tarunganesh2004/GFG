# H-Index

arr=[3,0,6,1,5]

def hIndex(citations):
    h=0
    arr.sort(reverse=True)

    for i in range(len(arr)):
        if i+1<=arr[i]:
            h=i+1
        else:
            break
    return h

print(hIndex(arr))