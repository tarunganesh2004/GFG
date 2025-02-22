# Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

s="(()"

def longestValidParentheses(s):
    stack = [-1]
    max_length = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

def anotherApproach(s):
    left = right = max_length = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_length = max(max_length, 2 * right)
        elif right >= left:
            left = right = 0
    left = right = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_length = max(max_length, 2 * left)
        elif left >= right:
            left = right = 0
    return max_length

print(longestValidParentheses(s))  # 2
print(anotherApproach(s))  # 2