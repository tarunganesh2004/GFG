# Next Greater Element

arr=[1,3,2,4]

# approach is to use stack
def nextGreaterElement(arr):
    st = []  # stack to hold indices
    res = [-1] * len(arr)  # initialize result list with -1

    for i in range(len(arr)):
        print(f"Current element: {arr[i]}, Stack: {st}")

        # While there is an element in the stack and the current element is greater than the one in the stack
        while st and arr[st[-1]] < arr[i]:
            index = st.pop()  # pop the index of the element
            res[index] = arr[i]  # update the result for that index
            print(f"Updated res[{index}] to {arr[i]}")

        st.append(i)  # push the current index onto the stack
        print(f"Stack after appending index {i}: {st}")

    return res


print(nextGreaterElement(arr))  # [3, 4, 4, -1]