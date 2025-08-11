# Maximum Non-Overlapping Odd Palindrome Sum

s="xyabacbcz"

def maxSum(s):

    def manacherArray(s):
        ms = "@#" + "#".join(s) + "#$"

        n = len(ms)
        p = [0] * n
        l = r = 0  # noqa: E741

        for i in range(1, n - 1):
            mirror = l + r - i
            if 0 <= mirror < n:
                p[i] = max(0, min(r - i, p[mirror]))

            while (
                i + p[i] + 1 < n
                and i - p[i] - 1 >= 0
                and ms[i + 1 + p[i]] == ms[i - 1 - p[i]]
            ):
                p[i] += 1

            if i + p[i] > r:
                l = i - p[i]  # noqa: E741
                r = i + p[i]

        return p
    
    def getLongest(cen,odd,p):
        pos=2*cen+2+(0 if odd else 1)
        return p[pos]
    
    n = len(s)
    leftMark = [1] * n
    rightMark = [1] * n

    p = manacherArray(s)

    # Fill leftMark: maximum odd-length palindrome
    # ending at or before each index
    for i in range(n):
        val = getLongest(i, 1, p)
        li = i + val // 2
        if li < n:
            leftMark[li] = max(leftMark[li], val)

    for i in range(n - 2, -1, -1):
        leftMark[i] = max(leftMark[i], leftMark[i + 1] - 2)

    for i in range(1, n):
        leftMark[i] = max(leftMark[i], leftMark[i - 1])

    # Fill rightMark: maximum odd-length
    # palindrome starting at or after each index
    for i in range(n - 1, -1, -1):
        val = getLongest(i, 1, p)
        ri = i - val // 2
        if ri >= 0:
            rightMark[ri] = max(rightMark[ri], val)

    for i in range(1, n):
        rightMark[i] = max(rightMark[i], rightMark[i - 1] - 2)

    for i in range(n - 2, -1, -1):
        rightMark[i] = max(rightMark[i], rightMark[i + 1])

    # Combine the two arrays to compute the
    # maximum sum of disjoint palindromes
    ans = 0
    for i in range(n - 1):
        ans = max(ans, leftMark[i] + rightMark[i + 1])

    return ans

print(maxSum(s))

"""Java Snippet:
public class MaxNonOverlappingOddPalindromeSum {
    public static int maxSum(String s) {
        int n = s.length();
        int[] leftMark = new int[n];
        int[] rightMark = new int[n];
        Arrays.fill(leftMark, 1);
        Arrays.fill(rightMark, 1);
        int[] p = manacherArray(s);
        for (int i = 0; i < n; i++) {
            int val = getLongest(i, true, p);
            int li = i + val / 2;
            if (li < n) {
                leftMark[li] = Math.max(leftMark[li], val);
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            leftMark[i] = Math.max(leftMark[i], leftMark[i + 1] - 2);
        }
        for (int i = 1; i < n; i++) {
            leftMark[i] = Math.max(leftMark[i], leftMark[i - 1]);
        }
        for (int i = n - 1; i >= 0; i--) {
            int val = getLongest(i, true, p);
            int ri = i - val / 2;
            if (ri >= 0) {
                rightMark[ri] = Math.max(rightMark[ri], val);
            }
        }
        for (int i = 1; i < n; i++) {
            rightMark[i] = Math.max(rightMark[i], rightMark[i - 1] - 2);
        }
        for (int i = n - 2; i >= 0; i--) {
            rightMark[i] = Math.max(rightMark[i], rightMark[i + 1]);
        }
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            ans = Math.max(ans, leftMark[i] + rightMark[i + 1]);
        }
        return ans;
    }
    private static int[] manacherArray(String s) {
        String ms = "@" + "#" + String.join("#", s.split("")) + "#$";
        int n = ms.length();
        int[] p = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n - 1; i++) {
            int mirror = l + r - i;
            if (mirror >= 0 && mirror < n) {
                p[i] = Math.max(0, Math.min(r - i, p[mirror]));
            }
            while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && ms.charAt(i + 1 + p[i]) == ms.charAt(i - 1 - p[i])) {
                p[i]++;
            }
            if (i + p[i] > r) {
                l = i - p[i];
                r = i + p[i];
            }
        }
        return p;
    }
    private static int getLongest(int cen, boolean odd, int[] p) {
        int pos = 2 * cen + 2 + (odd ? 0 : 1);
        return p[pos];
    }
    public static void main(String[] args) {
        String s = "xyabacbcz";
        System.out.println(maxSum(s));
    }
} """