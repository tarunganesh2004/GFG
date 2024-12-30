# Overlapping Intervals

arr = [[1, 3], [2, 4], [6, 8], [9, 10]]

def mergeOverLap(arr):
    arr.sort(key=lambda x:x[0])
    res=[arr[0]]
    for i in range(1,len(arr)):
        if res[-1][-1]>=arr[i][0]:
            res[-1][-1]=max(res[-1][-1],arr[i][-1])
        else:
            res.append(arr[i])

    return res

print(mergeOverLap(arr))