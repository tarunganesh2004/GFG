# Count Reverse Pairs

arr=[3,2,4,5,1,20]

def countReversePairsBrute(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count

# Count Reverse Pairs using Merge Sort
def countReversePairs(arr):
    def merging(arr,low,mid,high):
        count=0
        j=mid+1

        for i in range(low,mid+1):
            while j<=high and arr[i]>2*arr[j]:
                j+=1
            count+=(j-(mid+1))

        # merge step
        temp=[]
        left,right=low,mid+1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1

        while left<=mid:
            temp.append(arr[left])
            left+=1
        
        while right<=high:
            temp.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        return count
    
    def mergeSort(arr,low,high):
        if low>= high:
            return 0
        mid=low+ (high-low)//2
        count=(mergeSort(arr, low, mid) + 
                mergeSort(arr, mid + 1, high) + 
                merging(arr, low, mid, high))
        return count
    return mergeSort(arr, 0, len(arr) - 1)

print(countReversePairs(arr))

"""Java Snippet:
public class CountReversePairs {
    public static int countReversePairs(int[] arr) {
        return mergeSort(arr, 0, arr.length - 1);
    }

    private static int mergeSort(int[] arr, int low, int high) {
        if (low >= high) return 0;
        int mid = low + (high - low) / 2;
        int count = mergeSort(arr, low, mid) + mergeSort(arr, mid + 1, high);
        count += merging(arr, low, mid, high);
        return count;
    }

    private static int merging(int[] arr, int low, int mid, int high) {
        int count = 0;
        int j = mid + 1;

        for (int i = low; i <= mid; i++) {
            while (j <= high && arr[i] > 2 * arr[j]) {
                j++;
            }
            count += (j - (mid + 1));
        }

        // Merge step
        List<Integer> temp = new ArrayList<>();
        int left = low, right = mid + 1;
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.add(arr[left++]);
            } else {
                temp.add(arr[right++]);
            }
        }
        while (left <= mid) temp.add(arr[left++]);
        while (right <= high) temp.add(arr[right++]);

        for (int i = low; i <= high; i++) {
            arr[i] = temp.get(i - low);
        }
        return count;
    }
}
"""