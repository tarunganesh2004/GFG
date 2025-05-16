# Smallest range in K lists

n=5
k=3
arr = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]

def findSmallestRange(arr):
    import heapq
    k=len(arr)
    n=len(arr[0])
    min_heap = []
    max_val= float('-inf')

    for i in range(k):
        heapq.heappush(min_heap, (arr[i][0], i, 0))
        max_val = max(max_val, arr[i][0])

    range_start, range_end = float('-inf'), float('inf')
    while True:
        min_val,row, col = heapq.heappop(min_heap)

        if max_val - min_val < range_end - range_start:
            range_start, range_end = min_val, max_val

        if col + 1 == n:
            break
        next_val = arr[row][col + 1]
        heapq.heappush(min_heap, (next_val, row, col + 1))
        max_val = max(max_val, next_val)

    return [range_start, range_end]

print(findSmallestRange(arr))