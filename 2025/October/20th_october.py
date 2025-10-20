# Number of BST From array 

arr=[2,1,3]

def count_BST(arr):
    bsts=[1,1,2,5,14,42,132]
    n=len(arr)
    res=[]
    for i in range(n):
        x=0
        c=0
        for j in range(n):
            if arr[j]<arr[i]:
                x+=1
            elif arr[j]>arr[i]:
                c+=1
        res.append(bsts[x]*bsts[c])
    return res

print(count_BST(arr))