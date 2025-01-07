# Pair with given sum in a sorted array
# You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
# Note: pairs should have elements of distinct indexes. 


def countPairs(arr, target):
    # general 2 pointer approach returns only 2 pairs [1,5] and [-1,7], but here we need to return 3 pairs distinct elements with distinct indexes
    #  i.e 1 at index 1 and 5 at index 2, 1 at index 1 and 5 at index 3, -1 at index 0 and 7 at index 4 ==> 3 pairs
    n = len(arr)
    count = 0
    left = 0
    right = n - 1

    while left < right:
        cur_sum = arr[left] + arr[right]
        print(f"Checking pair ({arr[left]}, {arr[right]}) at indexes ({left}, {right})")
        print(f"Current sum = {cur_sum}")

        if cur_sum == target:
            print("Sum matches the target.")
            if arr[left] == arr[right]: # if both elements are same  then all elements between left and right can pair
                num_elements = right - left + 1
                pair_count = (num_elements * (num_elements - 1)) // 2
                print(
                    f"All elements are the same between indexes {left} and {right}. Total pairs = {pair_count}"
                )
                count += pair_count
                break
            else:
                # Count duplicates for arr[left]
                left_count = 1
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left_count += 1
                    left += 1
                print(f"Duplicates of {arr[left]} on the left: {left_count}")

                # Count duplicates for arr[right]
                right_count = 1
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right_count += 1
                    right -= 1
                print(f"Duplicates of {arr[right]} on the right: {right_count}")

                # Add pairs formed by duplicates
                pair_count = left_count * right_count
                print(f"Pairs formed with {arr[left]} and {arr[right]}: {pair_count}")
                count += pair_count

                # Move pointers inward
                left += 1
                right -= 1

        elif cur_sum > target:
            print(
                f"Current sum {cur_sum} is greater than target. Moving right pointer from {right} to {right - 1}."
            )
            right -= 1
        else:
            print(
                f"Current sum {cur_sum} is less than target. Moving left pointer from {left} to {left + 1}."
            )
            left += 1

        print(f"Current total pairs: {count}")
        print("-" * 50)

    return count



arr = [-1, 1, 5, 5, 7]
target = 6
print(f"Total Pairs: {countPairs(arr, target)}")
print("\n")

arr1 = [1, 1, 1, 1]
t1 = 2
print(f"Total Pairs: {countPairs(arr1, t1)}")