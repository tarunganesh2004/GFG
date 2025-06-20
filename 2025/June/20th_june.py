# Group Balls By Sequence

arr=[10,1,2,11]
k=2

def groupBalls(arr, k):
    from collections import Counter
    n=len(arr)
    if n % k != 0:
        return False  # Cannot group if total balls are not divisible by k
    
    arr.sort()
    # d=dict(Counter(list(arr)))
    d=Counter(arr)

    for item in arr:
        if d[item]==0:
            continue

        temp=k
        cur=item

        while temp>0:
            if cur not in d or d[cur]==0:
                return False
            d[cur]-=1
            cur+=1
            temp-=1
    return True


print(groupBalls(arr, k))  # Output: True