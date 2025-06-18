# All Palindromic Partitions

class Solution:
    def palinParts(self, s):
        return self.helper(s, 0)

    def helper(self, s, idx):
        if idx == len(s):
            return []

        ans = []

        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                curr = s[idx : i + 1]

                if i == len(s) - 1:
                    ans.append([curr])
                else:
                    for item in self.helper(s, i + 1):
                        ans.append([curr] + item)

        return ans

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
s="geeks"
print(Solution().palinParts(s))