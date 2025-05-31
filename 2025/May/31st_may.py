# Kth Element in Matrix

n=4
mat= [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
k = 3

def kth_smallest(mat,n,k):
    def count_less_equal(mid):
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if mat[row][col] <= mid:
                count += (row + 1)
                col += 1
            else:
                row -= 1
        return count

    low, high = mat[0][0], mat[n - 1][n - 1]
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

result = kth_smallest(mat, n, k)
print(result)  # Output: 27