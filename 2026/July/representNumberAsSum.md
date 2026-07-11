# DSA Notes — Represent a Number as Sum of Consecutive Natural Numbers

# Problem

Given an integer `n`, count the number of ways to represent it as the sum of **2 or more consecutive natural numbers**.

### Examples

```
Input : 10
Output: 1

10 = 1+2+3+4
```

```
Input : 15
Output: 3

15 = 1+2+3+4+5
15 = 4+5+6
15 = 7+8
```

---

# Constraints

```
1 <= n <= 10^8
```

Brute force should not be O(n²).

---

# First Observation

Question contains

```
Consecutive Numbers
```

Whenever you see

- consecutive integers
- consecutive natural numbers
- consecutive positive numbers

Think

```
Arithmetic Progression (AP)
```

---

# How to Think

Suppose one answer is

```
4+5+6
```

It has only two unknowns.

```
Starting Number
Length
```

Let's call them

```
start = a
length = k
```

Example

```
7+8

a=7
k=2
```

Example

```
4+5+6

a=4
k=3
```

Example

```
1+2+3+4+5

a=1
k=5
```

Every possible answer can be represented using

```
(a,k)
```

This is the biggest observation.

---

# Brute Force

Idea

Try every starting point.

```
1

1+2

1+2+3

1+2+3+4

...
```

Then

```
2

2+3

2+3+4

...
```

Continue until

```
start=n
```

Pseudo Code

```python
count=0

for start in range(1,n):

    total=0

    for x in range(start,n):

        total+=x

        if total==n:
            count+=1

        elif total>n:
            break
```

Time

```
Worst Case

O(n²)
```

Too slow.

---

# AP Formula

Sequence

```
a

a+1

a+2

...

a+k-1
```

Sum of AP

```
Sum = k(First+Last)/2
```

First

```
a
```

Last

```
a+k-1
```

Therefore

```
Sum

=

k(2a+k-1)/2
```

Since Sum=n

```
n=k(2a+k-1)/2
```

This is the main equation.

---

# Logic Derivation

Multiply by 2

```
2n=k(2a+k-1)
```

Divide by k

```
2n/k=2a+k-1
```

Move terms

```
2a=2n/k-k+1
```

Finally

```
a=(2n/k-k+1)/2
```

Now notice something important.

Instead of trying every

```
a
```

we can try every

```
k
```

and directly calculate

```
a
```

Huge optimization.

---

# Why Iterate over k instead of a?

Possible values of

```
a
```

```
1...

n
```

Almost

```
10^8
```

Too many.

Now think about

```
k
```

Can

```
k=100000
```

ever work for

```
n=15
```

No.

Because the smallest possible sequence of length 100000 is

```
1+2+3+...
```

already enormous.

So k has a much smaller search space.

---

# How did √(2n) come?

Smallest possible sum for length k

```
1+2+3+...+k
```

Formula

```
k(k+1)/2
```

This must be <= n.

```
k(k+1)/2 <= n
```

Multiply by 2

```
k(k+1)<=2n
```

Approximately

```
k²<=2n
```

Hence

```
k<=√2n
```

This becomes our loop limit.

Instead of

```
1...

100000000
```

we check only

```
1...

14142
```

for n=10⁸.

---

# Edge Conditions

We derived

```
a=(2n/k-k+1)/2
```

Now ask three questions.

---

## Condition 1

Can

```
2n
```

be divided by

```
k
```

exactly?

Example

```
30/4

=

7.5
```

Impossible.

So

```python
if (2*n)%k==0
```

Otherwise reject immediately.

---

## Condition 2

After computing

```
x=2n/k-k+1
```

Remember

```
2a=x
```

If

```
x=8
```

```
a=4
```

Good.

If

```
x=9
```

```
a=4.5
```

Impossible.

Therefore

```python
x%2==0
```

---

## Condition 3

Need

```
a>=1
```

Natural numbers cannot start from

```
0

-1

-2
```

Since

```
2a=x
```

Simply check

```python
x>0
```

---

# Complete Algorithm

```
For every possible length

↓

Check divisibility

↓

Compute x

↓

Check x is even

↓

Check x positive

↓

Answer++
```

---

# Dry Run

```
n=15
```

```
2n=30
```

Maximum

```
√30≈5
```

Loop

---

k=2

```
30%2==0
```

Yes

```
x=30//2-2+1

=14
```

Even

```
a=7
```

Answer

```
7+8
```

---

k=3

```
30%3==0
```

```
x=10-3+1

=8
```

Even

```
a=4
```

Answer

```
4+5+6
```

---

k=4

```
30%4!=0
```

Reject

---

k=5

```
30%5==0
```

```
x=6-5+1

=2
```

Even

```
a=1
```

Answer

```
1+2+3+4+5
```

Count

```
3
```

Correct.

---

# Optimized Code

```python
import math

def countWays(n):

    ans = 0

    # Try every possible length
    for k in range(2, int(math.sqrt(2*n)) + 1):

        # 2n must be divisible by k
        if (2*n) % k == 0:

            # x = 2a
            x = (2*n)//k - k + 1

            # x must be positive and even
            if x > 0 and x % 2 == 0:
                ans += 1

    return ans
```

---

# Code Building Line by Line

```python
ans=0
```

Store total answers.

---

```python
for k in range(2,int(math.sqrt(2*n))+1):
```

Try every possible sequence length.

Starts from

```
2
```

because question asks

```
2 or more numbers.
```

Ends at

```
√2n
```

because longer lengths are impossible.

---

```python
if (2*n)%k==0
```

Need

```
2n/k
```

to be an integer.

---

```python
x=(2*n)//k-k+1
```

This is

```
2a
```

derived mathematically.

---

```python
if x>0 and x%2==0
```

Need

```
a>0
```

Need

```
a
```

to be integer.

---

```python
ans+=1
```

Found one valid sequence.

---

# Complexity

Time

```
O(√n)
```

Space

```
O(1)
```

---

# Pattern Learned Today

Whenever question contains

```
Consecutive Numbers
```

ask yourself

```
Can I represent it as

Start + Length ?
```

If yes,

Write AP formula.

Convert the problem into an equation.

Instead of searching both variables,

iterate over the one having the smaller search space.

---

# Recognition Checklist

✅ Consecutive numbers

✅ Arithmetic progression

✅ Need number of ways

✅ Unknown start and length

✅ Derive equation

✅ Iterate over smaller variable

---

# Similar Interview Problems

1. Consecutive Numbers Sum (Leetcode 829)

2. Count ways to express N as consecutive integers

3. Find all consecutive sequences with given sum

4. Continuous Subarray Sum (different pattern—Prefix Sum)

5. Arithmetic Progression based sequence problems

---

# Common Mistakes

❌ Iterating over every starting number

❌ Forgetting that sequence length starts from 2

❌ Forgetting `x>0`

❌ Forgetting `x%2==0`

❌ Looping till n instead of √2n

❌ Using floating-point division instead of integer arithmetic

---

# Real-World Pattern

Many optimization problems have **two unknown variables**.

```
Cost = Price × Quantity

Area = Length × Breadth

AP Sum = Start + Length
```

Instead of brute-forcing both variables,

1. Build the equation.
2. Rearrange it.
3. Compute one variable from the other.
4. Iterate over the variable with the **smaller search space**.

This is a very common interview optimization technique.

---

# Permanent DSA Sheet

## Recognition

```
Consecutive Numbers
        ↓
Arithmetic Progression
        ↓
Represent as (start,length)
        ↓
Write AP Formula
        ↓
Set equal to target
        ↓
Solve for one variable
        ↓
Choose smaller search space
        ↓
Validate mathematical conditions
```

## Questions to Ask Yourself

```
1. Is this an AP?

2. What are the unknowns?

3. Can I derive an equation?

4. Which variable has fewer possibilities?

5. Can I calculate one variable directly?

6. What mathematical conditions make the answer valid?
```

## Biggest Lesson Today

> **Optimization did not come from the AP formula itself. It came from transforming the AP equation into a search over a single variable (`k`), because `k` has a much smaller search space (`√2n`) than the starting value (`a`).**