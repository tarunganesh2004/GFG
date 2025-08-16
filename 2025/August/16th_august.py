# Form the Largest Number

arr=[3, 30, 34, 5, 9]

def largestNumber(arr):
    # using custom sort
    from functools import cmp_to_key
    def compare(x,y):
        if x+y> y+x:
            return -1
        else:
            return 1
        
    numbers=[str(num) for num in arr]
    numbers.sort(key=cmp_to_key(compare))
    largest_num = ''.join(numbers)
    return largest_num if largest_num[0] != '0' else '0'

# other approach
def another(arr):
    arr=list(map(str, arr))
    def sort_key(x):
        return x * 10
    arr.sort(key=sort_key, reverse=True)
    largest_num = ''.join(arr)
    return largest_num if largest_num[0] != '0' else '0'

print(largestNumber(arr))
print(another(arr))


# """Java Snippet:
# import java.util.Arrays;
# import java.util.Comparator;
#
# public class LargestNumber {
#     public static String largestNumber(int[] nums) {
#         String[] numbers = new String[nums.length];
#         for (int i = 0; i < nums.length; i++) {
#             numbers[i] = String.valueOf(nums[i]);
#         }
#         Arrays.sort(numbers, new Comparator<String>() {
#             @Override
#             public int compare(String x, String y) {
#                 return (y + x).compareTo(x + y);
#             }
#         });
#         StringBuilder largestNum = new StringBuilder();
#         for (String num : numbers) {
#             largestNum.append(num);
#         }
#         return largestNum.charAt(0) == '0' ? "0" : largestNum.toString();
#     }
# }
# }
#
# """