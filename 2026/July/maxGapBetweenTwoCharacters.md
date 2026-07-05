# Max Gap Between Two Same Characters

## Problem Statement

Given a string `s`, find the **maximum number of characters between two occurrences of the same character**.

If no character appears more than once, return `-1`.

---

## Examples

### Example 1

```python
s = "socks"
```

Indexes:

```text
s o c k s
0 1 2 3 4
```

For character `'s'`:

```text
gap = 4 - 0 - 1 = 3
```

Answer:

```python
3
```

---

### Example 2

```python
s = "aa"
```

```text
a a
0 1
```

Gap:

```text
1 - 0 - 1 = 0
```

Answer:

```python
0
```

---

### Example 3

```python
s = "abc"
```

No repeated characters.

Answer:

```python
-1
```

---

# Understanding the Problem

The keyword is:

```text
MAX GAP
```

Not:

```text
same characters
```

Gap means:

```text
distance
between
farthest
difference
```

Whenever you see these words, think:

```text
INDEXES
```

NOT frequency.

---

# Common Mistake

Most people do:

```python
from collections import Counter
freq = Counter(s)
```

because they see:

```text
same characters
→ frequency
```

But frequency cannot tell us:

```text
where the characters occur
```

Example:

```python
Counter("socks")
```

Output:

```python
{'s':2,'o':1,'c':1,'k':1}
```

Can we compute the gap from this?

No.

Because we need:

```text
first index
last index
```

---

# Manual Thinking (Very Important)

Suppose:

```python
s = "socks"
```

How would you solve it on paper?

1. Look at index 0 (`s`)
2. Search to the right.
3. Found another `s` at index 4.
4. Gap:

```text
4 - 0 - 1 = 3
```

This immediately gives the brute force idea.

---

# Brute Force Approach

## Idea

Try every pair of indexes.

If characters are same:

```text
gap = j - i - 1
```

Update answer.

---

# Building the Logic

```text
for every i
    for every j > i
        if s[i] == s[j]
              gap = j - i - 1
              answer = max(answer, gap)
```

---

# Brute Force Code

```python
def maxCharGap(s):
    ans = -1
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                ans = max(ans, j - i - 1)

    return ans
```

---

# Dry Run

```python
s = "socks"
```

### i = 0

```text
j = 1 → o ≠ s
j = 2 → c ≠ s
j = 3 → k ≠ s
j = 4 → s = s
```

Gap:

```text
4 - 0 - 1 = 3
```

Answer:

```text
ans = 3
```

No other repeated characters.

Final Answer:

```text
3
```

---

# Complexity

### Time

```text
O(n²)
```

### Space

```text
O(1)
```

---

# Optimization

Observe:

For every character, we only need:

```text
first occurrence
current occurrence
```

We do NOT need all occurrences.

---

# Optimal Idea

Maintain a hashmap:

```python
first[ch] = first index of ch
```

While traversing:

### First time seeing character

Store its index.

### Seen before

Compute:

```text
gap = current_index - first_index - 1
```

Update answer.

---

# Dry Run

```python
s = "socks"
```

Initial:

```python
first = {}
ans = -1
```

---

### i = 0

```python
ch = 's'
first = {'s':0}
```

---

### i = 1

```python
ch = 'o'
first = {'s':0,'o':1}
```

---

### i = 2

```python
ch = 'c'
first = {'s':0,'o':1,'c':2}
```

---

### i = 3

```python
ch = 'k'
first = {'s':0,'o':1,'c':2,'k':3}
```

---

### i = 4

```python
ch = 's'
```

Already exists.

Gap:

```text
4 - 0 - 1 = 3
```

Update:

```python
ans = 3
```

---

# Optimal Code

```python
def maxCharGap(s):
    first = {}
    ans = -1

    for i, ch in enumerate(s):
        if ch not in first:
            first[ch] = i
        else:
            gap = i - first[ch] - 1
            ans = max(ans, gap)

    return ans
```

---

# Complexity Analysis

### Time

```text
O(n)
```

### Space

```text
O(k)
```

where:

```text
k = number of distinct characters
```

---

# Why We Store First Occurrence Only

Suppose:

```python
s = "abcaabcd"
```

Indexes:

```text
a b c a a b c d
0 1 2 3 4 5 6 7
```

For character `'a'`:

```text
0,3,4
```

Maximum gap:

```text
4 - 0 - 1 = 3
```

Keeping the earliest occurrence gives the largest distance.

So we never update:

```python
first['a']
```

---

# Important Interview Learning

Whenever the problem contains:

```text
distance
gap
between
nearest
farthest
length between positions
```

Immediately think:

```text
INDEXES
```

NOT:

```text
frequency
sorting
counting
```

---

# Pattern Learned

## Pattern Name

```text
First Occurrence HashMap Pattern
```

---

## Template

```python
mp = {}
ans = ...

for i, x in enumerate(arr):

    if x not in mp:
        mp[x] = i

    else:
        # use previous index
        something = i - mp[x]
        ans = update(ans, something)
```

---

# When to Recognize This Pattern

Questions involving:

- first occurrence
- last occurrence
- maximum distance
- minimum distance
- repeated elements
- nearest duplicate
- farthest duplicate
- longest span

---

# General Template

```python
mp = {}

for i in range(n):

    if arr[i] not in mp:
        mp[arr[i]] = i
    else:
        previous = mp[arr[i]]

        # calculate answer

        # update if necessary
```

---

# Similar Problems

---

## 1. Largest Subarray with Equal 0s and 1s
Leetcode 525

Pattern:

```text
Prefix Sum + First Occurrence HashMap
```

---

## 2. Longest Consecutive Sequence
Leetcode 128

Pattern:

```text
HashSet
```

---

## 3. Contains Duplicate II
Leetcode 219

Pattern:

```text
Store last occurrence index.
```

---

## 4. Longest Substring Without Repeating Characters
Leetcode 3

Pattern:

```text
Last occurrence + Sliding Window
```

---

## 5. First Unique Character in a String
Leetcode 387

Pattern:

```text
Frequency + Index
```

---

## 6. Degree of an Array
Leetcode 697

Pattern:

```text
Frequency + First Index + Last Index
```

---

## 7. Maximum Distance Between Equal Elements
Pattern:

```text
Store first occurrence and maximize distance.
```

---

# Final Takeaway

For every problem, ask these three questions:

```text
1. What exactly am I returning?
2. What information is needed to compute it?
3. How would I solve it manually on paper?
```

Then follow:

```text
Manual Solution
        ↓
Brute Force
        ↓
Optimization
```

This process is how almost every good DSA solution is discovered.