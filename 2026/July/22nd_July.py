# Minimum Deletions to Make Sorted

arr = [5, 6, 1, 7, 4]

# brute force
def bruteForce(arr):  # O(n^2)

    def recursion(
        idx, prev
    ):  # here cur_idx,prev_idx, instead of prev_idx we can use prev_val alsoo
        if idx == len(arr):
            return 0
        # not take
        not_take = recursion(idx + 1, prev)

        # take
        take = 0
        if prev == -1 or arr[idx] > arr[prev]:
            take = 1 + recursion(idx + 1, idx)  # replace prev with idx
        return max(take, not_take)

    return len(arr) - recursion(0, -1)  # -1 bcz there is no previous element


# memoization
"""
Here dp table ,
n*(n+1)
idx: 0 to n -->n
prev -- values -1 to n, so n+1,
"""


def memoization(arr):
    n = len(arr)
    memo = [[-1] * (n + 1) for _ in range(n)]

    def solve(idx, prev):
        if idx == len(arr):
            return 0

        if memo[idx][prev + 1] != -1:
            return memo[idx][prev + 1]

        not_take = solve(idx + 1, prev)
        take = 0
        if prev == -1 or arr[idx] > arr[prev]:
            take = 1 + solve(idx + 1, idx)

        memo[idx][prev + 1] = max(take, not_take)
        return memo[idx][prev + 1]

    return solve(0, -1)


# tabulation
def tabulation(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n)]
    # loop direction

    # cur depends on next , so idx --> bottom to top,

    # prev--> for given idx it can be -1 to idx-1

    for idx in range(n - 1, -1, -1):

        for prev in range(
            idx - 1, -2, -1
        ):  # prev can have -1 to idx-1, -2 bcz it excludes this value

            not_take = dp[idx + 1][prev]
            take = 0

            if prev == -1 or arr[idx] > arr[prev]:
                take = dp[idx + 1][idx + 1]  # column=prev+1, prev=idx

            dp[idx][prev + 1] = max(take, not_take)
    return len(arr)-dp[0][0]


# optimized approach is to use Binary search O(nlogn)

# tails[i] --> smallest posible ending value of an increasing subsequence of length i+1

"""

[4,2,6,3]

tails=[4]

next element 2,replace with 4 because, length 1 ending at 2 is better than length 1 ending at 4

tails=[2]

next element 6, 2<6 append tails=[2,6] -->means length 1 can end at 2, length 2 can end at 6

next element 3, this cannot extend length 2,but 3<6

replace 6, tails=[2,3] --> means length 2 ending at 3,is better than length 2 ending at 6

here the tails is sorted

so simply replace elements, that can form a better lis

so when a new number(x) occurs, we always need first element that is >=x

"""


def Optimized(arr):

    tails = []
    for num in arr:
        if not tails or num > tails[-1]:
            tails.append(num)

        else:  # here we can use bisect_left
            l = 0
            r = len(tails) - 1
            pos = -1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] >= num:
                    pos = mid
                    r = mid - 1
                else:
                    l = mid + 1
            tails[pos] = num

    return len(arr)-len(tails)


print(bruteForce(arr))

print(memoization(arr))
