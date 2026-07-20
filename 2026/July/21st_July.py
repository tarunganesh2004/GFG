# Maximum Reachable Index Difference

s="aaabcb"

# def maxIndexDifferenceBruteForce(s):
#     n=len(s)
#     ans=-1
#     for start in range(n):
#         if s[start]!='a':
#             continue

#         cur_idx=start
#         cur_char='a'
#         while True:
#             next_char=chr(ord(cur_char)+1)
#             next_idx=-1

#             for j in range(cur_idx+1,n):
#                 if s[j]==next_char:
#                     next_idx=j
#                     # break 
            
#             if next_idx==-1:
#                 break

#             # jump
#             cur_idx=next_idx
#             cur_char=next_char
        
#         ans=max(ans,cur_idx-start)
#     return ans # this is wrong brute force must try every possible jump

# print(maxIndexDifferenceBruteForce(s))

def bruteForce(s): # TLE
    n=len(s)
    def dfs(i):
        cur_char=s[i]

        next_char=chr(ord(cur_char)+1)

        best_end=i  
        for j in range(i+1,n):
            if s[j]==next_char:
                best_end=max(best_end,dfs(j))
        return best_end
    ans=-1
    # try every 'a' as starting point 
    for i in range(n):
        if s[i]=='a':
            ending_idx=dfs(i)
            ans=max(ans,ending_idx-i)
    return ans # this can be converted to memoization with memo=[-1]*n but still tle 

print(bruteForce(s))

def maxIndexDifference(s):
    n = len(s)

    # best[c] = farthest index reachable
    # from any occurrence of character c
    best = [-1] * 26

    answer = -1

    # Process from right to left
    for i in range(n - 1, -1, -1):

        current = ord(s[i]) - ord('a')

        # If current is not 'z',
        # find the next alphabet character
        if current < 25:

            next_char = current + 1

            if best[next_char] != -1:

                farthest = best[next_char]

            else:

                farthest = i

        else:

            farthest = i

        # Current index can reach this far
        best[current] = max(
            best[current],
            farthest
        )

        # We can start only from 'a'
        if current == 0:

            answer = max(
                answer,
                farthest - i
            )

    return answer