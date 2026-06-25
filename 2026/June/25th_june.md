# 25 June, Leetcode POTD

# 3737. Count Subarrays With Majority Element I

---

# Problem Statement

Given:

```python
nums
target
```

Count the number of subarrays where:

```text
target appears strictly more than half
of the subarray length
```

Example:

```text
nums = [1,2,2,3]
target = 2
```

Valid:

```text
[2]
[2]
[2,2]
[1,2,2]
[2,2,3]
```

Answer:

```text
5
```

---

# Step 1: Train Your Intuition

Whenever you see:

```text
Count subarrays
Count substrings
Number of intervals
```

Immediately think:

```text
Can I generate every subarray?
```

because every optimization starts from brute force.

---

# Step 2: Understanding Majority

Majority means:

```text
frequency(target) > length/2
```

Example:

```text
[2,2,1]

freq = 2
length = 3

2 > 1.5

Valid
```

Example:

```text
[2,1]

freq = 1
length = 2

1 > 1

False
```

Must be STRICTLY greater.

---

# Step 3: Brute Force Idea

Generate every subarray.

For every subarray:

```text
Count occurrences of target
Check majority condition
```

---

# Brute Force Code Template

```python
count = 0

for i in range(n):

    freq = 0

    for j in range(i, n):

        if nums[j] == target:
            freq += 1

        length = j - i + 1

        if freq > length // 2:
            count += 1
```

---

# Why Does This Work?

For every start:

```text
i
```

we extend:

```text
i
i..i+1
i..i+2
i..i+3
```

and maintain frequency.

---

# Complexity

Outer loop:

```text
O(n)
```

Inner loop:

```text
O(n)
```

Total:

```text
O(n²)
```

Space:

```text
O(1)
```

---

# Now Think Like an Interviewer

Question:

```text
What is repeatedly computed?
```

Answer:

```text
Frequency of target
Length
```

Length is easy.

Frequency can be maintained while expanding.

So brute force is already pretty decent.

---

# Important Observation

Condition:

```text
freq(target) > length/2
```

Multiply by 2:

```text
2 * freq(target) > length
```

Now replace:

```text
length = target_count + non_target_count
```

So:

```text
2 * target_count >
target_count + non_target_count
```

Move terms:

```text
target_count >
non_target_count
```

Huge observation.

---

# New Interpretation

Instead of majority:

Think:

```text
target_count
must be greater than
all other elements combined
```

Example:

```text
[2,2,3]

target_count = 2
others = 1

2 > 1
```

Valid.

---

# Convert Into Prefix Sum Problem

Transform array:

```text
target  -> +1
others  -> -1
```

Example:

```text
nums = [1,2,2,3]
target = 2
```

Convert:

```text
[-1,+1,+1,-1]
```

---

# Why?

Suppose subarray:

```text
[2,2,3]
```

Converted:

```text
[+1,+1,-1]
```

Sum:

```text
1
```

Positive.

Meaning:

```text
target_count > other_count
```

Exactly our condition.

---

# New Problem

Now becomes:

```text
Count subarrays
whose sum > 0
```

after transformation.

---

# Pattern Recognition

Whenever you see:

```text
More X than Y
Majority
Balance
Equal zeros and ones
More positives than negatives
```

Think:

```text
Convert into +1 / -1
```

This is a SUPER common pattern.

---

# Prefix Sum Construction

Example:

```text
[-1,+1,+1,-1]
```

Prefix:

```text
index : value

0 : 0
1 : -1
2 : 0
3 : 1
4 : 0
```

---

# Subarray Sum Formula

For subarray:

```text
l..r
```

sum:

```text
prefix[r+1] - prefix[l]
```

Need:

```text
prefix[r+1] > prefix[l]
```

---

# What Are We Counting?

For each current prefix:

```text
How many previous prefixes
are smaller than me?
```

This becomes a classic counting problem.

---

# Pattern Name

```text
Count pairs

prefix[j] > prefix[i]
where i < j
```

Very similar to:

```text
Count inversions
Count range sums
Count subarrays with positive sum
```

---

# Optimized Approach

Maintain:

```text
Frequency of previous prefix sums
```

Count:

```text
How many are smaller
than current prefix
```

Using:

```text
Fenwick Tree
BIT
Ordered Map
Balanced BST
```

---

# Why LeetCode Marks It Medium?

Constraint:

```text
n <= 1000
```

So O(n²) passes.

The intended solution for Part I is simply:

```text
O(n²)
```

No need for Fenwick Tree.

---

# Final Accepted Solution

```python
class Solution:
    def countSubarrays(self, nums, target):

        n = len(nums)
        ans = 0

        for i in range(n):

            freq = 0

            for j in range(i, n):

                if nums[j] == target:
                    freq += 1

                length = j - i + 1

                if freq > length / 2:
                    ans += 1

        return ans
```

---

# Dry Run

Example:

```text
nums = [1,2,2,3]
target = 2
```

Start:

```text
i = 0
```

Expand:

```text
[1]

freq=0
length=1

0 > 0.5

False
```

---

```text
[1,2]

freq=1
length=2

1 > 1

False
```

---

```text
[1,2,2]

freq=2
length=3

2 > 1.5

True
```

count = 1

---

```text
[1,2,2,3]

freq=2
length=4

2 > 2

False
```

---

Continue similarly.

Final:

```text
5
```

---

# Pattern Identification Cheat Sheet

If problem says:

```text
Count subarrays
```

Think:

```text
Brute force first
Prefix Sum second
```

---

If problem says:

```text
Frequency
Majority
More than half
```

Think:

```text
Can I convert into counts?
```

---

If problem says:

```text
More A than B
```

Think:

```text
A -> +1
B -> -1
```

---

If problem says:

```text
Equal A and B
```

Think:

```text
A -> +1
B -> -1

Need sum = 0
```

---

# Real Interview Patterns

## Pattern 1

```text
Count subarrays with equal 0s and 1s
```

Transform:

```text
0 -> -1
1 -> +1
```

Need:

```text
sum = 0
```

---

## Pattern 2

```text
More 1s than 0s
```

Transform:

```text
1 -> +1
0 -> -1
```

Need:

```text
sum > 0
```

---

## Pattern 3

```text
Majority element
```

Transform:

```text
target -> +1
others -> -1
```

Need:

```text
sum > 0
```

---

## Pattern 4

```text
Equal vowels and consonants
```

Transform:

```text
vowel -> +1
consonant -> -1
```

Need:

```text
sum = 0
```

---

# Golden Rule

When stuck on subarray problems:

```text
1. Write brute force
2. Identify condition
3. Convert condition into math
4. Express using prefix sums
5. Look for a known pattern
```

This process solves nearly 80% of medium-level subarray problems.
