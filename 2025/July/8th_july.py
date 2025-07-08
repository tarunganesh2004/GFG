# Next Element with Greater Frequency

arr=[2,1,1,3,2,1]
def nextGreaterFrequency(arr):
    from collections import Counter
    
    freq = Counter(arr)
    n = len(arr)
    res = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
            stack.pop()
        if stack:
            res[i] = arr[stack[-1]]
        stack.append(i)
    
    return res

print(nextGreaterFrequency(arr))