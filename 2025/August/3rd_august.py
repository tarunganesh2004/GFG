# 2D Difference Array 

mat=[[1,2,3],
     [1,1,0],
     [4,-2,2]]

opr=[[2,0,0,1,1],[-1,1,0,2,2]]

# brute force
def bruteForce(mat,opr):
    # n=len(mat)
    # m=len(mat[0])
    for i in range(len(opr)):
        v,r1,c1,r2,c2=opr[i]
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                mat[r][c] += v
    return mat

# optimized is to use 2D difference array 
def optimized(mat,opr):
    n=len(mat)
    m=len(mat[0])
    diff=[[0 for _ in range(m+1)] for _ in range(n+1)]
    print("Initial Difference Matrix:")
    for row in diff:
        print(row)
    
    # for each operation mark 4 corners
    for v,r1,c1,r2,c2 in opr:
        print(f"Applying operation: value={v}, r1={r1}, c1={c1}, r2={r2}, c2={c2}")
        diff[r1][c1]+=v
        if c2+1<m:
            diff[r1][c2+1]-=v
        if r2+1<n:
            diff[r2+1][c1]-=v
        if r2+1<n and c2+1<m:
            diff[r2+1][c2+1]+=v
    print("Difference Matrix after operations:")
    for row in diff:
        print(row)

    # now row-wise prefix sum
    for r in range(n):
        for c in range(1,m):
            diff[r][c] += diff[r][c-1]
    print("Row-wise Prefix Sum:")
    for row in diff:
        print(row)

    # now column-wise prefix sum
    for c in range(m):
        for r in range(1,n):
            diff[r][c] += diff[r-1][c]
    print("Column-wise Prefix Sum:")
    for row in diff:
        print(row)

    # now add diff to mat
    for r in range(n):
        for c in range(m):
            mat[r][c] += diff[r][c]
    return mat

print(bruteForce(mat,opr))
print(optimized(mat, opr))


"""
Java Snippet:

public static List<List<Integer>> apply2DDiff(int[][] mat, int[][] opr) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] diff = new int[m + 1][n + 1];
        for (int[] operation : opr) {
            int val = operation[0];
            int r1 = operation[1];
            int c1 = operation[2];
            int r2 = operation[3];
            int c2 = operation[4];

            diff[r1][c1] += val;
            if (r2 + 1 < m) {
                diff[r2 + 1][c1] -= val;
            }
            if (c2 + 1 < n) {
                diff[r1][c2 + 1] -= val;
            }
            if (r2 + 1 < m && c2 + 1 < n) {
                diff[r2 + 1][c2 + 1] += val;
            }

        }

        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                diff[i][j] += diff[i][j - 1];
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < m; i++) {
                diff[i][j] += diff[i - 1][j];
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(mat[i][j] + diff[i][j]);
            }
            result.add(row);
        }
        return result;
    }
"""