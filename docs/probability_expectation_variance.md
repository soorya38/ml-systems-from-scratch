# Descriptive Statistics

## 1.1 Why do we need descriptive statistics?

Imagine someone gives you:

```text
[2, 3, 3, 5, 7]
```

Looking at five numbers isn't difficult.

But real ML datasets may contain:

```text
10,000 rows
100,000 rows
10 million rows
```

So we need a way to answer:

> **"What does this data look like?"**

Descriptive statistics gives us compact ways to summarize data.

For example:

```text
Data:     [2, 3, 3, 5, 7]

Center:   roughly 4
Spread:   roughly from 2 to 7
Common:   3
```

The important point:

**Descriptive statistics describes the data we already have.**

It doesn't, by itself, try to predict unseen data.

---

## 1.2 Dataset and observations

A **dataset** is a collection of data.

For example, suppose we record the ages of five people:

```text
Age = [20, 22, 21, 25, 30]
```

Each individual value is an **observation** (or data point).

```text
20 → observation
22 → observation
21 → observation
25 → observation
30 → observation
```

The variable we're measuring is:

```text
Age
```

So:

```text
Variable:       Age
Observations:   20, 22, 21, 25, 30
```

In ML, a dataset usually contains many variables called **features**.

For example:

| Person | Age | Height | Hours studied |
| ------ | --: | -----: | ------------: |
| A      |  20 |    170 |             3 |
| B      |  22 |    175 |             5 |
| C      |  21 |    168 |             4 |

Here:

* each **row** is an observation
* `Age`, `Height`, and `Hours studied` are variables/features

---

# 1.3 Mean

The **mean** is what we commonly call the average.

Suppose:

```text
[2, 3, 3, 5, 7]
```

Add everything:

```text
2 + 3 + 3 + 5 + 7 = 20
```

There are 5 observations.

Therefore:

```text
mean = 20 / 5
     = 4
```

Mathematically:

[
\text{mean} = \frac{\text{sum of observations}}{\text{number of observations}}
]

So the mean tells us roughly where the data is **centered**.

### Another example

```text
Age = [20, 22, 21, 25, 30]
```

[
\text{mean}
===========

\frac{20+22+21+25+30}{5}
]

[
=\frac{118}{5}
=23.6
]

So the average age is:

```text
23.6
```

### Important: the mean can be affected by outliers

Compare:

```text
[2, 3, 3, 5, 7]
```

Mean:

```text
4
```

Now change `7` to `100`:

```text
[2, 3, 3, 5, 100]
```

Mean:

[
\frac{2+3+3+5+100}{5}
=====================

22.6
]

One extreme value moved the mean from:

```text
4 → 22.6
```

That's why the mean can be sensitive to **outliers**.

---

# 1.4 Median

The **median** is the middle value after sorting the data.

Example:

```text
[7, 2, 5, 3, 3]
```

First sort:

```text
[2, 3, 3, 5, 7]
```

The middle value is:

```text
3
```

Therefore:

```text
median = 3
```

### Why is median useful?

Consider:

```text
[2, 3, 3, 5, 100]
```

Mean:

```text
22.6
```

Median:

```text
3
```

The median is much less affected by the extreme value `100`.

So:

**Mean → sensitive to outliers**

**Median → more resistant to outliers**

---

## Even number of observations

Suppose:

```text
[2, 4, 6, 8]
```

There isn't one middle value.

The two middle values are:

```text
4 and 6
```

Take their average:

[
\frac{4+6}{2}=5
]

Therefore:

```text
median = 5
```

---

# 1.5 Mode

The **mode** is the value that occurs most frequently.

Example:

```text
[2, 3, 3, 5, 7]
```

`3` occurs twice.

Everything else occurs once.

Therefore:

```text
mode = 3
```

Mode is particularly useful when the most common value matters.

For example:

```text
shirt sizes = [M, L, M, S, M, L]
```

The mode is:

```text
M
```

We won't spend much time on mode because mean, median, and spread are generally more important for our ML foundations.

---

# 1.6 Range

The **range** gives us a simple measure of how far the data extends.

[
\text{range} = \text{maximum} - \text{minimum}
]

For:

```text
[2, 3, 3, 5, 7]
```

Maximum:

```text
7
```

Minimum:

```text
2
```

Therefore:

[
7-2=5
]

```text
range = 5
```

---

# 1.7 Spread

Knowing the center isn't enough.

Consider:

```text
A = [4, 5, 5, 6]

B = [1, 3, 7, 9]
```

Both have mean:

### A

[
\frac{4+5+5+6}{4}=5
]

### B

[
\frac{1+3+7+9}{4}=5
]

Same mean:

```text
5
```

But look at the values:

```text
A:      4  5  5  6
        ↑  ↑  ↑  ↑
       close to 5

B:   1     3     7     9
     ↑     ↑     ↑     ↑
       farther from 5
```

Dataset B has much more **spread**.

So:

> **Center tells us where the data is. Spread tells us how much the observations vary around that center.**

We'll later use **variance** to quantify this spread.

---

# 1.8 Number-line intuition

Consider:

```text
1----2----3----4----5----6----7----8
     •    •    •    •         •
```

The observations are concentrated around the middle.

The **center** tells us approximately where the points are concentrated.

The **spread** tells us how far apart they are.

This distinction becomes extremely important when we introduce variance.

---

# 1.9 Worked Examples

### Example 1

```text
[2, 4, 6, 8]
```

Mean:

[
\frac{2+4+6+8}{4}=5
]

Median:

[
\frac{4+6}{2}=5
]

Range:

[
8-2=6
]

---

### Example 2

```text
[1, 2, 2, 3, 12]
```

Mean:

[
\frac{1+2+2+3+12}{5}
====================

4
]

Median:

```text
2
```

Range:

[
12-1=11
]

Notice how the outlier `12` pulls the mean upward.

---

### Example 3

Which dataset has greater spread?

```text
A = [4, 5, 5, 6]

B = [1, 3, 7, 9]
```

Both have mean `5`.

Ranges:

```text
A: 6 - 4 = 2
B: 9 - 1 = 8
```

So B clearly has greater spread.

---

# 1.10 Connection to Machine Learning

Descriptive statistics is one of the first things we do when examining an ML dataset.

We might ask:

```text
What is the average age?
What is the typical house price?
What is the range of a feature?
Are there unusual values?
How variable is this feature?
```

This helps with:

* understanding datasets
* finding unusual observations
* understanding feature behavior
* understanding scale and spread
* preprocessing

For example, if a dataset contains:

```text
Age = [21, 22, 20, 23, 400]
```

Descriptive statistics immediately makes the suspicious value `400` noticeable.

---

# Exercises — Descriptive Statistics

### Easy

**1.** Calculate the mean:

```text
[2, 4, 6, 8]
```

**2.** Calculate the median:

```text
[7, 2, 5, 1, 4]
```

**3.** Calculate the range:

```text
[3, 8, 2, 10, 5]
```

### Medium

**4.** Calculate the mean and median:

```text
[2, 3, 3, 4, 20]
```

Which better represents the typical value?

**5.** Which dataset has greater spread?

```text
A = [4, 5, 5, 6]
B = [2, 4, 6, 8]
```

**6.** Which statistic is likely more useful for:

```text
[10, 11, 10, 12, 100]
```

Mean or median? Why?

### Hard

**7.** Suppose:

```text
A = [2, 4, 6, 8]
```

You replace `8` with `100`.

What happens to:

* mean?
* median?
* range?

---

# 2. Probability Fundamentals

Descriptive statistics asks:

> **"What does our data look like?"**

Probability asks a different question:

> **"How do we represent uncertainty?"**

For example:

```text
Will it rain tomorrow?
Will this email be spam?
Will this patient have a particular outcome?
Will this ML model classify an image as a cat?
```

Probability lets us represent uncertainty numerically.

---

# 2.1 Probability

Probability ranges from:

[
0 \leq P(A) \leq 1
]

where:

```text
0 → impossible
1 → certain
```

Examples:

```text
P(impossible event) = 0

P(certain event) = 1
```

A probability of:

```text
0.7
```

means the event has probability 70%.

---

# 2.2 Experiment and Outcome

An **experiment** is a process that produces an uncertain result.

Example:

```text
Roll a die
```

One possible result is:

```text
4
```

That result is an **outcome**.

Possible outcomes:

```text
1, 2, 3, 4, 5, 6
```

The collection of all possible outcomes is the **sample space**.

[
S={1,2,3,4,5,6}
]

An **event** is a collection of outcomes we're interested in.

For example:

> Roll an even number.

Event:

[
A={2,4,6}
]

---

# 2.3 Basic Probability

If outcomes are equally likely:

[
P(A)=
\frac{\text{number of favorable outcomes}}
{\text{total number of possible outcomes}}
]

For a fair die:

```text
Sample space = {1,2,3,4,5,6}
```

Probability of rolling `4`:

```text
favorable outcomes = 1
total outcomes = 6
```

Therefore:

[
P(4)=\frac16
]

Probability of rolling an even number:

```text
{2,4,6}
```

There are 3 favorable outcomes.

[
P(\text{even})=\frac36=\frac12
]

---

# 2.4 Complement

Sometimes it is easier to calculate the probability that something **doesn't** happen.

The complement of event A means:

```text
A does NOT happen
```

The rule is:

[
P(\text{not }A)=1-P(A)
]

Suppose:

[
P(A)=0.7
]

Then:

[
P(\text{not }A)=1-0.7=0.3
]

So:

```text
A happens     → 70%
A doesn't     → 30%
```

---

# 2.5 Addition Rule

Suppose:

```text
A = rolling a 2
B = rolling a 5
```

A die cannot simultaneously show 2 and 5.

These events are **mutually exclusive**.

For mutually exclusive events:

[
P(A\text{ or }B)=P(A)+P(B)
]

Therefore:

[
P(2\text{ or }5)
================

# \frac16+\frac16

# \frac26

\frac13
]

---

## General case

Sometimes A and B can happen together.

Then:

[
P(A\cup B)
==========

P(A)+P(B)-P(A\cap B)
]

The notation means:

```text
A ∪ B → A or B
A ∩ B → A and B
```

Why subtract the intersection?

Suppose:

```text
A = students who play football
B = students who play cricket
```

Someone who plays both football and cricket belongs to both groups.

If we calculate:

```text
number in A + number in B
```

we count those people twice.

So we subtract the overlap once.

---

# 2.6 Conditional Probability

This is one of the most important probability ideas for ML.

Suppose we ask:

> What is the probability that A happens **given that we already know B happened?**

We write:

[
P(A\mid B)
]

Read it as:

> **Probability of A given B.**

The formula is:

[
P(A\mid B)
==========

\frac{P(A\cap B)}{P(B)}
]

Where:

* (P(A\mid B)) = probability of A given B
* (P(A\cap B)) = probability that both A and B happen
* (P(B)) = probability of B

### Simple example

Suppose a class has:

```text
10 students
```

Of these:

```text
6 are male
4 are female
```

Suppose:

```text
3 males play football
```

What is:

> Probability a randomly selected student plays football, given that they are male?

We only consider the male students now.

```text
male students = 6
male football players = 3
```

Therefore:

[
P(\text{football}\mid\text{male})
=================================

# \frac36

0.5
]

The important idea:

> **Conditional probability changes the information we are working with.**

---

# 2.7 Independence

Two events are **independent** if knowing that one occurred doesn't change the probability of the other.

Consider two separate coin flips.

First flip:

```text
Heads / Tails
```

Second flip:

```text
Heads / Tails
```

Knowing the first flip was heads tells us nothing about the second flip.

Therefore they are independent.

For independent events:

[
P(A\cap B)=P(A)P(B)
]

For two coin flips:

[
P(H_1\cap H_2)
==============

# \frac12\times\frac12

\frac14
]

---

# 2.8 Independent vs Mutually Exclusive

This is a **very important distinction**.

### Mutually exclusive

Two events cannot happen together.

Example:

```text
Roll a 2
Roll a 5
```

A single die roll cannot be both.

Therefore:

```text
P(A ∩ B) = 0
```

### Independent

One event doesn't affect the probability of the other.

Example:

```text
First coin flip = Heads
Second coin flip = Heads
```

They can happen together.

So:

```text
mutually exclusive ≠ independent
```

In fact, events that are mutually exclusive and have non-zero probability cannot be independent.

---

# 2.9 Probability Tree

Two coin flips:

```text
             First
            /     \
           H       T
          / \     / \
         H   T   H   T
```

Each branch has probability:

```text
1/2
```

Therefore:

```text
HH = 1/2 × 1/2 = 1/4
HT = 1/2 × 1/2 = 1/4
TH = 1/2 × 1/2 = 1/4
TT = 1/2 × 1/2 = 1/4
```

This is a simple way to visualize uncertainty.

---

# 2.10 Worked Probability Examples

### Example 1 — Basic probability

A die is rolled.

Probability of rolling greater than 4?

Favorable:

```text
{5, 6}
```

Therefore:

[
P(X>4)=\frac26=\frac13
]

---

### Example 2 — Complement

Probability of rolling a 6:

[
P(6)=\frac16
]

Probability of **not** rolling a 6:

[
1-\frac16=\frac56
]

---

### Example 3 — Addition

Probability of rolling `1 or 6`:

[
\frac16+\frac16
===============

\frac13
]

---

### Example 4 — Conditional probability

Suppose:

```text
8 students are male
5 of those males play football
```

Then:

[
P(\text{football}\mid\text{male})
=================================

\frac58
]

---

# Machine Learning Connection

Probability appears everywhere in ML.

For example, a classifier might output:

```text
Cat: 0.85
Dog: 0.10
Bird: 0.05
```

These represent probabilities assigned to possible outcomes.

Probability helps us reason about:

* classification
* uncertain predictions
* noisy data
* probabilistic predictions
* probability distributions
* likelihood

A key idea is:

> ML often doesn't simply say "this is definitely class A." It can represent uncertainty about the prediction.

---

# Exercises — Probability

### Easy

**1.** A fair die is rolled. What is the probability of rolling an odd number?

**2.** A fair coin is flipped. What is the probability of **not** getting heads?

**3.** Write the sample space for rolling a six-sided die.

### Medium

**4.** A die is rolled. What is:

[
P(2\text{ or }5)
]

**5.** In a group of 10 students, 6 are male and 3 of those males play football. What is:

[
P(\text{football}\mid\text{male})
]

**6.** Two fair coins are flipped. What is the probability of getting heads on both?

### Hard

**7.** Two fair coins are flipped.

What is the probability of getting **at least one head**?

**8.** Are the following events mutually exclusive?

```text
A = rolling an even number
B = rolling a number greater than 3
```

Are they independent?

Explain your reasoning.

---

# 3. Random Variables

Before expectation, we need one new idea.

Imagine rolling a die.

The outcome could be:

```text
1, 2, 3, 4, 5, 6
```

We can define:

[
X=\text{number shown on the die}
]

Then X can take:

```text
1, 2, 3, 4, 5, 6
```

Here, **X is a random variable**.

In simple terms:

> A random variable is a variable whose value depends on the outcome of a random process.

For our die:

```text
Roll → X

1 → X = 1
2 → X = 2
3 → X = 3
...
6 → X = 6
```

This gives us a bridge between:

```text
PROBABILITY
     ↓
RANDOM VARIABLES
     ↓
EXPECTATION
     ↓
VARIANCE
```

---

# 4. Expectation

Suppose we roll a die.

What is its "typical" value?

You might initially think:

```text
3.5
```

But you can never actually roll `3.5`.

So what does `3.5` mean?

It is the **expected value**.

Expectation is essentially a **probability-weighted average**.

---

# 4.1 Expected Value of a Fair Die

For a fair die:

```text
X = 1, 2, 3, 4, 5, 6
```

Every outcome has probability:

[
\frac16
]

Therefore:

[
E[X]
====

1\left(\frac16\right)
+
2\left(\frac16\right)
+
3\left(\frac16\right)
+
4\left(\frac16\right)
+
5\left(\frac16\right)
+
6\left(\frac16\right)
]

Factor out (1/6):

[
E[X]
====

\frac{1+2+3+4+5+6}{6}
]

# [

# \frac{21}{6}

3.5
]

Therefore:

[
\boxed{E[X]=3.5}
]

---

# 4.2 What does expectation actually mean?

This is important.

**Expected value does not necessarily mean an outcome we will observe.**

For the die:

```text
Possible values:
1 2 3 4 5 6
```

Expected value:

```text
3.5
```

But:

```text
3.5 cannot be rolled.
```

Instead, think of expectation as the **long-run average**.

If you repeatedly roll the die many times and calculate the average, that average tends toward approximately:

```text
3.5
```

So:

> **Expectation represents the probability-weighted center of possible outcomes.**

---

# 4.3 Two-outcome Example

Suppose:

```text
X = 10 with probability 0.2
X = 0  with probability 0.8
```

Then:

[
E[X]
====

10(0.2)+0(0.8)
]

[
=2
]

So:

[
\boxed{E[X]=2}
]

Even though `2` is not an outcome, it represents the long-run average.

---

# 4.4 Non-uniform Example

Suppose:

```text
X = 1 with probability 0.5
X = 2 with probability 0.3
X = 10 with probability 0.2
```

Then:

[
E[X]
====

1(0.5)+2(0.3)+10(0.2)
]

[
=0.5+0.6+2
]

[
=3.1
]

Therefore:

[
\boxed{E[X]=3.1}
]

The value `10` has a relatively small probability, but it still contributes significantly to the expectation.

---

# 5. Linearity of Expectation

Now we introduce some algebra that appears frequently in ML.

Suppose:

[
Y=aX+b
]

Then:

[
\boxed{E[aX+b]=aE[X]+b}
]

In plain English:

* multiplying X by (a) multiplies its expected value by (a)
* adding (b) adds (b) to its expected value

### Example

Suppose:

[
E[X]=5
]

Define:

[
Y=2X+3
]

Then:

[
E[Y]
====

2E[X]+3
]

[
=2(5)+3
]

[
=13
]

So:

[
\boxed{E[Y]=13}
]

---

## Addition

Expectation also distributes across addition:

[
\boxed{E[X+Y]=E[X]+E[Y]}
]

Importantly, **independence is not required for this rule**.

Suppose:

[
E[X]=4
]

and:

[
E[Y]=7
]

Then:

[
E[X+Y]=4+7=11
]

This simple property becomes extremely useful when analyzing ML expressions.

---

# 6. Variance

Expectation tells us about the **center**.

But remember our earlier datasets:

```text
A = [4, 5, 5, 6]

B = [1, 3, 7, 9]
```

Both have mean:

```text
5
```

But B is much more spread out.

We need a numerical measure of this spread.

That is **variance**.

---

# 6.1 Intuition

To calculate variance:

### Step 1

Find the mean.

### Step 2

Find how far each value is from the mean.

### Step 3

Square those differences.

### Step 4

Average them.

Why square?

Because otherwise positive and negative differences could cancel.

For example:

```text
Mean = 5

Value 3 → difference = -2
Value 7 → difference = +2
```

If we simply averaged:

```text
(-2 + 2) / 2 = 0
```

That incorrectly suggests there is no spread.

Squaring gives:

```text
(-2)² = 4
(+2)² = 4
```

Now the deviations don't cancel.

---

# 6.2 Variance Formula

The variance of X is:

[
\boxed{\operatorname{Var}(X)=E[(X-E[X])^2]}
]

Read this as:

> **Variance is the expected squared distance from the mean.**

Let's decode it:

```text
E[ ... ]       → take the expected value
X              → the random variable
E[X]           → its mean
X - E[X]       → distance from the mean
(...)²         → square the distance
```

---

# 6.3 Variance Example

Take:

```text
A = [4, 5, 5, 6]
```

Mean:

[
E[X]=5
]

Distances from the mean:

```text
4 - 5 = -1
5 - 5 =  0
5 - 5 =  0
6 - 5 = +1
```

Square them:

```text
1
0
0
1
```

Average:

[
\frac{1+0+0+1}{4}
=================

# \frac24

0.5
]

Therefore:

[
\boxed{\operatorname{Var}(X)=0.5}
]

---

# 6.4 Compare Dataset B

```text
B = [1, 3, 7, 9]
```

Mean:

[
E[X]=5
]

Distances:

```text
1 - 5 = -4
3 - 5 = -2
7 - 5 = +2
9 - 5 = +4
```

Squared:

```text
16
4
4
16
```

Average:

[
\frac{16+4+4+16}{4}
===================

# \frac{40}{4}

10
]

Therefore:

[
\boxed{\operatorname{Var}(X)=10}
]

Compare:

```text
A variance = 0.5
B variance = 10
```

This numerically confirms what we saw visually:

```text
A → tightly concentrated
B → widely spread
```

---

# 6.5 Mean vs Variance

Keep this distinction very clear:

### Mean / Expectation

> **Where are the values centered?**

### Variance

> **How spread out are the values around that center?**

For example:

```text
Dataset A
      ••••
      ↑
    center
    small spread
```

versus:

```text
•          •
     ↑
   center
     ↑
•          •
large spread
```

---

# 6.6 Standard Deviation

Variance is measured in **squared units**.

For that reason, we often also use the **standard deviation**:

[
\text{standard deviation}
=========================

\sqrt{\text{variance}}
]

For dataset A:

[
\sqrt{0.5}\approx0.707
]

For dataset B:

[
\sqrt{10}\approx3.162
]

You don't need to study standard deviation deeply yet.

Just remember:

```text
Variance       → average squared spread
Standard dev.  → square root of variance
```

---

# 7. Useful Variance Identity

Calculating deviations from the mean every time can be inconvenient.

A very useful identity is:

[
\boxed{
\operatorname{Var}(X)
=====================

E[X^2]-(E[X])^2
}
]

This is extremely important in probability and ML.

Notice the difference:

[
E[X^2]
]

means:

> square X first, then take expectation.

Whereas:

[
(E[X])^2
]

means:

> take expectation first, then square it.

These are **not generally the same**.

---

## Example

For:

```text
X = [4,5,5,6]
```

We already know:

[
E[X]=5
]

Square each value:

```text
16, 25, 25, 36
```

Therefore:

[
E[X^2]
======

\frac{16+25+25+36}{4}
]

# [

# \frac{102}{4}

25.5
]

Now:

[
(E[X])^2=5^2=25
]

Therefore:

[
\operatorname{Var}(X)
=====================

# 25.5-25

0.5
]

Same result as before.

---

# 8. Variance Algebra

Now we can understand how variance behaves when we transform a random variable.

---

## 8.1 Adding a constant

Suppose:

[
Y=X+10
]

Every value moves 10 units to the right.

Example:

```text
X:  2  4  6
Y: 12 14 16
```

The center changes.

But the distances between values don't change.

Therefore:

[
\boxed{\operatorname{Var}(X+b)=\operatorname{Var}(X)}
]

Adding a constant changes the **center**, not the **spread**.

---

# 8.2 Multiplying by a constant

Suppose:

[
Y=2X
]

Every distance from the mean doubles.

But variance uses **squared distances**.

So:

```text
distance → ×2
squared distance → ×4
```

Therefore:

[
\boxed{\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)}
]

Notice the square on (a).

### Example

Suppose:

[
\operatorname{Var}(X)=3
]

and:

[
Y=2X+5
]

Then:

[
\operatorname{Var}(Y)
=====================

2^2\operatorname{Var}(X)
]

[
=4(3)
]

[
=12
]

The `+5` doesn't matter for variance.

---

# 8.3 Sum of Independent Random Variables

If X and Y are independent:

[
\boxed{
\operatorname{Var}(X+Y)
=======================

\operatorname{Var}(X)+\operatorname{Var}(Y)
}
]

For example:

[
\operatorname{Var}(X)=2
]

[
\operatorname{Var}(Y)=3
]

If they're independent:

[
\operatorname{Var}(X+Y)=2+3=5
]

We won't go into covariance yet.

---

# 9. Machine Learning Connection

Now let's connect everything.

## Descriptive statistics

Before training a model, we inspect the data.

We might calculate:

```text
mean
median
range
spread
```

This helps us understand the dataset.

---

## Probability

ML often deals with uncertainty.

A classifier might say:

```text
P(cat) = 0.85
P(dog) = 0.15
```

Instead of simply saying:

```text
cat
```

Probability lets the model express confidence/uncertainty.

---

## Expectation

Expectation appears when we talk about an **average outcome over uncertainty**.

One important ML example is expected loss:

[
E[L]
]

Informally:

> What loss do we expect on average?

This connects probability to model evaluation and optimization.

---

## Variance

Variance tells us about variability.

It can help us reason about:

* noisy data
* variability in observations
* uncertainty
* variation in model behavior

It also gives the foundation for the basic intuition behind **bias and variance**.

We are **not** doing the full bias-variance decomposition yet.

---

# 10. The Big Picture

You can now connect the concepts:

```text
DATA
 │
 ├── observations
 │
 ▼
DESCRIPTIVE STATISTICS
 │
 ├── mean      → center
 ├── median    → center
 ├── mode      → common value
 ├── range     → simple spread
 └── spread    → how much values vary
 │
 ▼
UNCERTAINTY
 │
 ▼
PROBABILITY
 │
 ├── outcomes
 ├── sample space
 ├── events
 ├── complement
 ├── addition
 ├── conditional probability
 └── independence
 │
 ▼
RANDOM VARIABLE
 │
 ▼
EXPECTATION
 │
 └── probability-weighted center
 │
 ▼
VARIANCE
 │
 └── spread around expectation
 │
 ▼
ML
 │
 ├── datasets
 ├── noisy observations
 ├── uncertain predictions
 ├── expected loss
 └── probabilistic models
```

---

# 11. Exercises — Expectation and Variance

## Easy

**1.** A random variable has:

```text
X = 0 with probability 0.5
X = 10 with probability 0.5
```

Calculate:

[
E[X]
]

---

**2.** A random variable has:

```text
X = 1 with probability 0.5
X = 3 with probability 0.5
```

Calculate:

[
E[X]
]

and

[
E[X^2]
]

---

**3.** Calculate the variance of:

```text
X = [2, 4, 6]
```

---

## Medium

**4.**

Suppose:

[
E[X]=5
]

Calculate:

[
E[2X+3]
]

---

**5.**

Suppose:

[
\operatorname{Var}(X)=4
]

Calculate:

[
\operatorname{Var}(3X+10)
]

---

**6.**

A random variable has:

```text
X = 0 with probability 0.5
X = 2 with probability 0.5
```

Calculate:

[
E[X]
]

[
E[X^2]
]

and:

[
\operatorname{Var}(X)
]

using:

[
\operatorname{Var}(X)=E[X^2]-(E[X])^2
]

---

## Hard

**7.**

Suppose:

[
E[X]=4,\qquad E[Y]=6
]

Calculate:

[
E[2X+3Y+5]
]

---

**8.**

Suppose X and Y are independent:

[
\operatorname{Var}(X)=2
]

[
\operatorname{Var}(Y)=5
]

Calculate:

[
\operatorname{Var}(X+Y)
]

---

**9.**

Consider:

```text
X = 1 with probability 0.25
X = 5 with probability 0.75
```

Calculate:

1. (E[X])
2. (E[X^2])
3. (\operatorname{Var}(X))

Then explain what the variance tells you about the possible values of X.

---

# 12. Expected Answers

## Descriptive Statistics

**1.**

[
\frac{2+4+6+8}{4}=5
]

**Answer: 5**

**2.**

Sorted:

```text
[1,2,4,5,7]
```

**Answer: 4**

**3.**

[
10-2=8
]

**Answer: 8**

**4.**

Mean:

[
\frac{2+3+3+4+20}{5}=6.4
]

Median:

```text
3
```

**Answer:** Median better represents the typical value because `20` is an outlier.

**5.**

```text
A range = 6 - 4 = 2
B range = 8 - 2 = 6
```

**Answer: B**

**6.**

**Answer: Median**, because the extreme value `100` strongly affects the mean.

**7.**

Replacing `8` with `100`:

* mean increases substantially
* median changes from `5` to `4.5`
* range increases from `6` to `98`

---

# Probability Answers

**1.**

Odd outcomes:

```text
{1,3,5}
```

[
P=\frac36=\frac12
]

**Answer: (1/2)**

**2.**

[
P(\text{not heads})=1-\frac12=\frac12
]

**Answer: (1/2)**

**3.**

[
{1,2,3,4,5,6}
]

**4.**

[
P(2\text{ or }5)
================

# \frac16+\frac16

\frac13
]

**5.**

[
P(\text{football}\mid\text{male})
=================================

# \frac36

\frac12
]

**6.**

[
P(HH)
=====

# \frac12\frac12

\frac14
]

**7.**

Use the complement:

[
P(\text{at least one H})
========================

1-P(TT)
]

[
=1-\frac14
==========

\frac34
]

**8.**

A and B are **not mutually exclusive**, because a roll can be both even and greater than 3:

```text
4 or 6
```

They are also **not independent** because:

[
P(A)=\frac12
]

but:

[
P(A\mid B)=\frac23
]

Since these aren't equal, the events aren't independent.

---

# Expectation & Variance Answers

**1.**

[
E[X]=0(0.5)+10(0.5)=5
]

**Answer: 5**

**2.**

[
E[X]=1(0.5)+3(0.5)=2
]

[
E[X^2]=1^2(0.5)+3^2(0.5)=5
]

**Answers:**

```text
E[X]   = 2
E[X²]  = 5
```

**3.**

Mean:

[
E[X]=4
]

Variance:

[
\frac{(2-4)^2+(4-4)^2+(6-4)^2}{3}
=================================

# \frac{4+0+4}{3}

\frac83
]

**Answer: (8/3)**

**4.**

[
E[2X+3]
=======

# 2(5)+3

13
]

**Answer: 13**

**5.**

[
\operatorname{Var}(3X+10)
=========================

# 3^2(4)

36
]

**Answer: 36**

**6.**

[
E[X]=0(0.5)+2(0.5)=1
]

[
E[X^2]=0^2(0.5)+2^2(0.5)=2
]

[
\operatorname{Var}(X)=2-1^2=1
]

**Answers:**

```text
E[X]      = 1
E[X²]     = 2
Var(X)    = 1
```

**7.**

[
E[2X+3Y+5]
==========

2E[X]+3E[Y]+5
]

[
=2(4)+3(6)+5
============

31
]

**Answer: 31**

**8.**

Because X and Y are independent:

[
\operatorname{Var}(X+Y)
=======================

# 2+5

7
]

**Answer: 7**

**9.**

[
E[X]
====

# 1(0.25)+5(0.75)

4
]

[
E[X^2]
======

# 1^2(0.25)+5^2(0.75)

19
]

Therefore:

[
\operatorname{Var}(X)
=====================

# 19-4^2

3
]

**Answers:**

```text
E[X]       = 4
E[X²]      = 19
Var(X)     = 3
```

The variance tells us that the values aren't concentrated exactly at the mean; there is meaningful spread between `1` and `5`.

---

# 13. What You Should Understand Before Moving On

You should now be able to explain these without memorizing definitions.

### Descriptive Statistics

* **Dataset** → collection of observations
* **Observation** → one data point
* **Mean** → arithmetic center
* **Median** → middle value
* **Mode** → most frequent value
* **Range** → maximum − minimum
* **Spread** → how much observations vary
* **Outlier** → unusual/extreme observation

### Probability

* **Probability** → numerical representation of uncertainty
* **Outcome** → one possible result
* **Sample space** → all possible outcomes
* **Event** → outcome or collection of outcomes we're interested in
* **Complement** → event not happening
* **Conditional probability** → probability given additional information
* **Independent events** → one doesn't change the probability of the other
* **Mutually exclusive** → cannot happen together

### Expectation

* **Random variable** → numerical value determined by a random process
* **Expectation** → probability-weighted average
* (E[X]) → expected value of X
* Expected value doesn't have to be an actually possible outcome
* (E[aX+b]=aE[X]+b)
* (E[X+Y]=E[X]+E[Y])

### Variance

* **Variance** → spread around the expected value
* (\operatorname{Var}(X)=E[(X-E[X])^2])
* (\operatorname{Var}(X)=E[X^2]-(E[X])^2)
* Standard deviation = square root of variance
* (\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X))
* For independent X and Y:
  [
  \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
  ]

---

# 14. The Five Expressions You Should Be Comfortable Reading

When you eventually see these in ML, they shouldn't look intimidating:

### 1. (P(A\mid B))

> "Probability that A happens, given that B is known to have happened."

### 2. (E[X])

> "The probability-weighted average value of X."

### 3. (\operatorname{Var}(X))

> "How much X varies around its expected value."

### 4. (E[X^2]-(E[X])^2)

> "A convenient way to calculate variance."

### 5. (E[aX+b])