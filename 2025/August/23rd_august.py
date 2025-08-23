# Allocate Minimum Pages

arr=[12,34,67,90]
k=2

def findPages(arr,k):
    def is_valid(arr,n,k,max_pages):
        students=1
        cur_pages=0

        for pages in arr:
            if pages>max_pages:
                return False
            if cur_pages+pages>max_pages:
                students+=1
                cur_pages=pages
                if students>k:
                    return False
            else:
                cur_pages+=pages
        return True

    n=len(arr)
    low=max(arr)
    high=sum(arr)
    result=-1

    while low<=high:
        mid=(low+high)//2
        if is_valid(arr,n,k,mid):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(findPages(arr,k))