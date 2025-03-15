# Coin Change ,return the minimum number of coins that you need to make up that amount.

coins = [1, 2, 5]
amount = 11


# recursion
def coinChange(coins, amount):
    def helper(coins, n, amount):
        if amount == 0:
            return 0
        if amount < 0 or n == 0:
            return float("inf")

        # include
        include = helper(coins, n, amount - coins[n - 1])
        if include != float("inf"):
            include += 1
        # exclude
        exclude = helper(coins, n - 1, amount)
        return min(include, exclude)

    return helper(coins, len(coins), amount)


# using lru_cache
def coinChangeMemoi(coins, amount):
    from functools import lru_cache

    coins = tuple(coins)

    @lru_cache(None)
    def helper(n, remaining_amt):
        if remaining_amt == 0:
            return 0
        if remaining_amt < 0 or n == 0:
            return float("inf")

        # include
        include = helper(n, remaining_amt - coins[n - 1])
        if include != float("inf"):
            include += 1
        # exclude
        exclude = helper(n - 1, remaining_amt)
        return min(include, exclude)

    return helper(len(coins), amount)


# memoization
def coinchangememo(coins, amount, memo={}):
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    if amount in memo:
        return memo[amount]

    # include
    include = float("inf")
    for coin in coins:
        if amount >= coin:
            include = min(include, 1 + coinchangememo(coins, amount - coin, memo))

    memo[amount] = include
    return include


print(coinChange(coins, amount))  # 3
print(coinChangeMemoi(coins, amount))  # 3

print(coinchangememo(coins, amount))  # 3