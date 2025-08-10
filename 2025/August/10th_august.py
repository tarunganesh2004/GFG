# Palindromic Substrings

s="abaab"

# brute force
def bruteForce(s):
    count=0
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            substr= s[i:j]
            if len(substr)>1 and substr==substr[::-1]:
                count+=1
    return count

# Optimized approach using Expanding Around Center
def optimized(s):
    n=len(s)
    count=0

    def expandAroundCenter(left, right):
        nonlocal count 
        while left>=0 and right <n and s[left]==s[right]:
            if right-left+1 > 1:
                count+=1 # only count if length > 1
            left -= 1
            right += 1
    
    for center in range(n):
        # Odd length palindromes
        expandAroundCenter(center, center)
        # Even length palindromes
        expandAroundCenter(center, center + 1)
    return count


print(bruteForce(s))
print(optimized(s))

"""Java Snippet:
public class PalindromicSubstrings {
    public static int countPalindromicSubstrings(String s) {
        int n = s.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            // Odd length palindromes
            count += expandAroundCenter(s, i, i);
            // Even length palindromes
            count += expandAroundCenter(s, i, i + 1);
        }
        return count;
    }

    private static int expandAroundCenter(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            if (right - left + 1 > 1) { // Only count if length > 1
                count++;
            }
            left--;
            right++;
        }
        return count;
    }

   
}
"""