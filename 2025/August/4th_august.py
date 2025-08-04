# Maximum sum Rectangle in a 2D matrix

mat=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]

# brute force
def bruteForce(mat): # O(n^2 * m^2)
    n=len(mat)
    m=len(mat[0])
    max_sum=float('-inf')
    for r1 in  range(n): # top row
        for r2 in range(r1,n): # bottom row
            for c1 in range(m): # left column
                for c2 in range(c1,m): # right column
                    cur_sum=0
                    for r in range(r1,r2+1):
                        for c in range(c1,c2+1):
                            cur_sum += mat[r][c]
                    max_sum = max(max_sum, cur_sum)

                    
    return max_sum

# optimized is to use Kadane's algorithm on 1D array
def optimized(mat):
    n=len(mat)
    m=len(mat[0])
    max_sum=float('-inf')
    def kadane(arr):
        max_ending_here=max_so_far=arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    

    for top in range(n):
        temp=[0]*m 
        for bottom in range(top,n):
            for col in range(m):
                temp[col] += mat[bottom][col]

            cur_max=kadane(temp)
            max_sum = max(max_sum, cur_max)
    return max_sum

print(bruteForce(mat))
print(optimized(mat))

"""
Java Snippet:
public static int maxRectangle(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int maxSum = Integer.MIN_VALUE;
        for (int top = 0; top < n; top++) {
            int[] temp = new int[m];
            for (int bottom = top; bottom < n; bottom++) {
                for (int col = 0; col < m; col++) {
                    temp[col] += mat[bottom][col];
                }
                int curMax = kadane(temp);
                maxSum = Math.max(maxSum, curMax);
            }
        }
        return maxSum;
    }

    public static int kadane(int[] arr) {
        int maxSoFar = arr[0];
        int maxEndingHere = arr[0];
        for (int i = 1; i < arr.length; i++) {
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }
"""