# Sort by Absolute Difference

x=7
arr=[10,5,3,9,2]

def sort_by_absolute_difference(arr, x):
    # Sort the array based on the absolute difference from x
    arr.sort(key=lambda num: abs(num - x))
    return arr

# using merge sort
def merge_sort(arr,x):
    if len(arr)<=1:
        return arr
    mid= len(arr) // 2
    left = merge_sort(arr[:mid],x)
    right = merge_sort(arr[mid:],x)

    return merge(left, right, x)

def merge(left, right, x):
    res=[]
    i=j=0

    while i<len(left) and j<len(right):
        if abs(left[i] - x) <= abs(right[j] - x):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res    

print(sort_by_absolute_difference(arr, x))
print(merge_sort(arr, x))

"""
# Java Snippet:
# import java.util.Arrays;
# import java.util.Comparator;
#
# public class SortByAbsoluteDifference {
#     public static int[] sortByAbsoluteDifference(int[] arr, int x) {
#         Integer[] numbers = Arrays.stream(arr).boxed().toArray(Integer[]::new);
#         Arrays.sort(numbers, new Comparator<Integer>() {
#             @Override
#             public int compare(Integer a, Integer b) {
#                 return Integer.compare(Math.abs(a - x), Math.abs(b - x));
#             }
#         });
#         return Arrays.stream(numbers).mapToInt(Integer::intValue).toArray();
#     }
# }
"""