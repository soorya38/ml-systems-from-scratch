# Topic: Vector Operations

## Description

A **vector** is an ordered collection of numbers. In machine learning, a vector usually represents one object using several numerical features.

For example:

`x = [2, 3]`

can represent one object with two features:

* `2` = feature 1
* `3` = feature 2

The **dimension** of a vector is the number of values it contains. So `[2, 3]` is a **2-dimensional vector**.

The fundamental operations are:

* **Addition:** combine corresponding values.
* **Subtraction:** find the difference between corresponding values.
* **Scalar multiplication:** multiply every value by the same number. A **scalar** is just a single number.
* **Dot product:** multiply corresponding values and add the results. It produces a single number.

For vectors

`a = [a₁, a₂, ..., aₙ]`

and

`b = [b₁, b₂, ..., bₙ]`,

their dot product is:

`a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ`

where `·` means dot product and `n` is the number of dimensions.

Intuitively, the dot product measures how strongly two vectors **align** with each other.

---

## Visual Example

Think of a 2D vector as an arrow starting at the origin:

```text
y
↑
|          • (3,2)
|        ↗
|      ↗
|    ↗
|  ↗
| •
+----------------→ x
(0,0)
```

`[3, 2]` means:

* move 3 units horizontally
* move 2 units vertically

So the vector describes both **direction** and **magnitude**.

---

## Worked Examples

### Example 1 — Vector Addition

Given:

`a = [2, 3]`

`b = [4, 1]`

Add corresponding values:

```text
a + b
= [2 + 4, 3 + 1]
= [6, 4]
```

Why?

The first component of `a` combines with the first component of `b`, and the second combines with the second.

**Answer: `[6, 4]`**

---

### Example 2 — Vector Subtraction

Given:

`a = [5, 7]`

`b = [2, 3]`

```text
a - b
= [5 - 2, 7 - 3]
= [3, 4]
```

Why?

Subtraction tells us how much the corresponding values differ.

**Answer: `[3, 4]`**

---

### Example 3 — Scalar Multiplication

Given:

`a = [2, 3]`

Multiply by scalar `4`:

```text
4a
= [4×2, 4×3]
= [8, 12]
```

Every component is scaled by the same amount.

**Answer: `[8, 12]`**

Geometrically, multiplying by `4` makes the arrow four times as long while keeping its direction.

---

### Example 4 — Dot Product

Given:

`a = [2, 3]`

`b = [4, 1]`

Multiply corresponding values:

```text
2 × 4 = 8
3 × 1 = 3
```

Then add:

```text
a · b
= 8 + 3
= 11
```

**Answer: `11`**

The important idea is:

```text
vectors → multiply corresponding components → add → one number
```

---

## Machine Learning Connection

Suppose:

```text
x = [2, 3]
w = [0.5, 0.2]
```

`x` could represent two features of a house:

* `2` bedrooms
* `3` bathrooms

`w` contains the importance assigned to each feature.

The dot product is:

```text
w · x
= (0.5 × 2) + (0.2 × 3)
= 1 + 0.6
= 1.6
```

This weighted combination of features appears constantly in **linear regression, neural networks, and optimization**.

---

## Exercises

### Easy

1. Calculate:

   `[2, 5] + [3, 1]`

2. Calculate:

   `[7, 4] - [2, 3]`

3. Calculate:

   `3[2, 4]`

### Medium

4. Calculate the dot product:

   `[2, 3] · [4, 2]`

5. Given:

   `a = [1, 2, 3]`

   `b = [4, 0, 2]`

   Calculate `a + b`.

6. Given:

   `x = [2, 4]` and `w = [0.5, 0.25]`, calculate `w · x`.

### Hard

7. Find `x` if:

   `[2, 5] + x = [7, 9]`

8. Which is larger?

   `[1, 2] · [3, 4]`

   or

   `[2, 1] · [3, 4]`

   Calculate both before deciding.

---

## Expected Answers

1. Answer: `[5, 6]`

2. Answer: `[5, 1]`

3. Answer: `[6, 12]`

4. Answer: `2×4 + 3×2 = 14`

5. Answer: `[5, 2, 5]`

6. Answer: `0.5×2 + 0.25×4 = 2`

7. Answer: `[5, 4]`

8. Answer: First = `11`, second = `10`; first is larger.

---

## What I Should Know Before Moving On

You are ready to continue if you can:

* Explain what a vector and its dimension are.
* Add and subtract vectors component-by-component.
* Multiply a vector by a scalar.
* Calculate a dot product.
* Explain that a dot product turns two vectors into one number.
* Understand a vector as an arrow with direction and magnitude.

---

# Topic: Matrix Basics

## Description

A **matrix** is a rectangular arrangement of numbers.

For example:

```text
A = [ 1  2  3
      4  5  6 ]
```

A matrix has:

* **Rows** — horizontal lines.
* **Columns** — vertical lines.

This matrix has **2 rows and 3 columns**, so its shape is:

`2 × 3`

A matrix is useful when we need to store many vectors together.

For example, a dataset can be represented as:

```text
       feature 1  feature 2  feature 3
sample 1    2          5          1
sample 2    4          3          2
sample 3    1          6          4
```

This is a `3 × 3` matrix.

The basic matrix operations you need are:

* accessing elements
* addition/subtraction
* scalar multiplication
* transpose
* identity matrix

---

## Visual Example

Consider:

```text
A = [ 2  4  6
      1  3  5 ]
```

Visualizing the structure:

```text
        columns
         ↓  ↓  ↓
       [ 2  4  6 ] ← row 1
       [ 1  3  5 ] ← row 2
```

It has:

```text
2 rows × 3 columns
```

The element in row 2, column 3 is:

```text
A₂₃ = 5
```

---

## Worked Examples

### Example 1 — Matrix Shape and Elements

Given:

```text
A = [ 2  7
      4  1
      3  5 ]
```

There are:

* 3 rows
* 2 columns

Therefore:

```text
Shape = 3 × 2
```

The element in row 2, column 1 is:

```text
A₂₁ = 4
```

**Answer: shape `3 × 2`, element `4`**

---

### Example 2 — Matrix Addition

Given:

```text
A = [ 1  2
      3  4 ]

B = [ 5  6
      7  8 ]
```

Add corresponding elements:

```text
A + B
= [ 1+5   2+6
    3+7   4+8 ]

= [ 6   8
   10  12 ]
```

Matrices must have the same shape for this operation.

**Answer:**

```text
[ 6   8
  10  12 ]
```

---

### Example 3 — Scalar Multiplication

Given:

```text
A = [ 1  2
      3  4 ]
```

Multiply by `3`:

```text
3A
= [ 3×1  3×2
    3×3  3×4 ]

= [ 3   6
    9  12 ]
```

Every element is multiplied by the scalar.

---

### Example 4 — Transpose

Transpose means **turn rows into columns**.

Given:

```text
A = [ 1  2  3
      4  5  6 ]
```

After transposing:

```text
Aᵀ = [ 1  4
       2  5
       3  6 ]
```

The original shape is:

```text
2 × 3
```

The transpose has shape:

```text
3 × 2
```

---

### Example 5 — Identity Matrix

The `2 × 2` identity matrix is:

```text
I = [ 1  0
      0  1 ]
```

It behaves like the number `1` when multiplying compatible vectors or matrices.

For example:

```text
I [3] = [3]
  [5]   [5]
```

The values are unchanged.

---

## Machine Learning Connection

Suppose each row represents a training example:

```text
X = [ 2  3
      4  1
      5  2 ]
```

You can interpret this as:

```text
          feature 1  feature 2
sample 1      2          3
sample 2      4          1
sample 3      5          2
```

So:

* rows = examples
* columns = features

This is one of the most common ways data is represented in ML.

---

## Exercises

### Easy

1. What is the shape of:

```text
[ 1  2  3
  4  5  6 ]
```

2. What is the element in row 2, column 3?

```text
[ 4  7  2
  8  1  5 ]
```

3. Calculate:

```text
2[ 1  3
    4  5 ]
```

### Medium

4. Calculate:

```text
[ 1  2
  3  4 ]

+

[ 5  1
  2  6 ]
```

5. Find the transpose:

```text
[ 1  2  3
  4  5  6 ]
```

6. A dataset has 100 samples and 5 features. What is the shape of its data matrix if each row represents one sample?

### Hard

7. A matrix has shape `4 × 3`.

   * How many rows?
   * How many columns?
   * How many total elements?

8. Is this matrix addition possible?

```text
A: 2 × 3
B: 3 × 2
```

Explain why.

---

## Expected Answers

1. Answer: `2 × 3`

2. Answer: `5`

3. Answer:

```text
[2  6
 8 10]
```

4. Answer:

```text
[6 3
 5 10]
```

5. Answer:

```text
[1 4
 2 5
 3 6]
```

6. Answer: `100 × 5`

7. Answer: `4 rows`, `3 columns`, `12 elements`

8. Answer: No. Matrix addition requires the same shape.

---

## What I Should Know Before Moving On

You are ready to continue if you can:

* Explain rows, columns, and matrix shape.
* Access a matrix element using its row and column.
* Add and subtract matrices of the same shape.
* Multiply a matrix by a scalar.
* Transpose a matrix.
* Recognize the identity matrix.
* Understand how a dataset can be represented as a matrix.

---

# Topic: Matrix Multiplication

## Description

Matrix multiplication is initially confusing because it is **not** ordinary element-by-element multiplication.

Its purpose is to combine information from rows and columns.

The central operation is:

> **Take a row from the first matrix and a column from the second matrix, calculate their dot product, and put the result into the output matrix.**

For example:

```text
[ a  b ] [ e  f ]
[ c  d ] [ g  h ]
```

The top-left output element is:

```text
a×e + b×g
```

### Dimension compatibility

If:

```text
A = m × n
B = n × p
```

then:

```text
AB = m × p
```

The **inside dimensions must match**:

```text
(m × n)(n × p)
       ↑   ↑
       must match
```

The output takes the **outside dimensions**:

```text
(m × n)(n × p)
 → m × p
```

---

## Visual Example

Consider:

```text
A = [ 1  2 ]       B = [ 3
      4  5 ]             6 ]
```

To calculate `AB`:

```text
row of A       column of B

[1  2]    ×    [3]
               [6]

= 1×3 + 2×6
= 15
```

So:

```text
AB = [15
      42]
```

The matrix-vector multiplication produces a new vector.

The key pattern is:

```text
row × column → one number
```

---

## Worked Examples

### Example 1 — Simple Matrix × Vector

Given:

```text
A = [ 2  1
      3  4 ]

x = [ 5
      2 ]
```

Calculate `Ax`.

For the first output value, use row 1:

```text
[2  1] · [5  2]
= 2×5 + 1×2
= 12
```

For the second output value, use row 2:

```text
[3  4] · [5  2]
= 3×5 + 4×2
= 23
```

Therefore:

```text
Ax = [12
      23]
```

Notice that each row of `A` interacts with the entire vector `x`.

---

### Example 2 — Full Matrix Multiplication

Given:

```text
A = [ 1  2
      3  4 ]

B = [ 5  6
      7  8 ]
```

Both are `2 × 2`.

The output is therefore also `2 × 2`.

Calculate each position separately.

Top-left:

```text
[1  2] · [5  7]
= 1×5 + 2×7
= 19
```

Top-right:

```text
[1  2] · [6  8]
= 1×6 + 2×8
= 22
```

Bottom-left:

```text
[3  4] · [5  7]
= 3×5 + 4×7
= 43
```

Bottom-right:

```text
[3  4] · [6  8]
= 3×6 + 4×8
= 50
```

Therefore:

```text
AB = [19  22
      43  50]
```

---

### Example 3 — Understanding the Shape

Suppose:

```text
A = 2 × 3
B = 3 × 4
```

Can we multiply them?

Yes.

```text
(2 × 3)(3 × 4)
      ↑   ↑
      3 = 3
```

The output shape is the outside dimensions:

```text
2 × 4
```

So:

```text
AB = 2 × 4
```

This lets you determine the output shape **before doing any calculations**.

---

### Example 4 — Matrix × Matrix Step-by-Step

Given:

```text
A = [ 1  2  3
      4  5  6 ]

B = [ 1  2
      0  1
      2  3 ]
```

Shapes:

```text
A = 2 × 3
B = 3 × 2
```

Therefore:

```text
AB = 2 × 2
```

Top-left:

```text
[1 2 3] · [1 0 2]
= 1×1 + 2×0 + 3×2
= 7
```

Top-right:

```text
[1 2 3] · [2 1 3]
= 1×2 + 2×1 + 3×3
= 13
```

Bottom-left:

```text
[4 5 6] · [1 0 2]
= 4×1 + 5×0 + 6×2
= 16
```

Bottom-right:

```text
[4 5 6] · [2 1 3]
= 4×2 + 5×1 + 6×3
= 31
```

Therefore:

```text
AB = [ 7  13
      16  31 ]
```

---

## Machine Learning Connection

Matrix multiplication is fundamental to neural networks and linear models.

Suppose:

```text
x = [2
     3]
```

and:

```text
W = [0.5  0.2
     0.1  0.4]
```

Then:

```text
Wx
```

is:

```text
[0.5  0.2] [2]
[0.1  0.4] [3]
```

First output:

```text
0.5×2 + 0.2×3 = 1.6
```

Second output:

```text
0.1×2 + 0.4×3 = 1.4
```

Therefore:

```text
Wx = [1.6
      1.4]
```

A common ML expression is:

```text
Wx + b
```

where:

* `W` = weights
* `x` = input features
* `b` = bias vector

Matrix multiplication allows the model to take many input features and produce many weighted outputs simultaneously.

This is essentially the same idea as the dot product you learned earlier, performed across multiple rows at once.

---

## Exercises

### Easy

1. Calculate:

```text
[1  2] [3]
       [4]
```

2. What is the output shape?

```text
(2 × 3)(3 × 5)
```

3. Can these matrices be multiplied?

```text
(2 × 3)(4 × 2)
```

### Medium

4. Calculate:

```text
[1  2] [3  4]
[0  1] [5  6]
```

5. Calculate:

```text
[2  1  3] [1]
            [2]
            [4]
```

6. Given:

```text
A = 3 × 2
B = 2 × 4
```

What is the shape of `AB`?

### Hard

7. Calculate:

```text
A = [1  2
     2  1]

x = [3
     4]
```

Find `Ax`.

8. Explain why `(2 × 3)(3 × 4)` is valid but `(2 × 3)(2 × 4)` is not.

---

## Expected Answers

1. Answer: `11`

2. Answer: `2 × 5`

3. Answer: No; `3 ≠ 4`.

4. Answer:

```text
[13 16
  5  6]
```

5. Answer: `2×1 + 1×2 + 3×4 = 16`

6. Answer: `3 × 4`

7. Answer:

```text
[11
 10]
```

8. Answer: The inner dimensions must match. `3 = 3` in the first case; `3 ≠ 2` in the second.

---

## What I Should Know Before Moving On

You are ready to continue if you can:

* Explain why matrix multiplication exists.
* Calculate a row × column dot product.
* Determine whether two matrices can be multiplied.
* Determine the output shape before calculating.
* Perform matrix × vector multiplication.
* Perform matrix × matrix multiplication.
* Understand that matrix multiplication can apply many weighted combinations simultaneously.
* Understand the basic meaning of `Wx + b`.

---

# Topic: Vector Norms

## Description

A **norm** measures the size or length of a vector.

For example:

```text
v = [3, 4]
```

Its ordinary geometric length is `5`.

A norm gives us a way to turn a vector into a **single non-negative number representing its size**.

Two norms are especially useful in ML:

### L1 norm

Add the absolute values of the components:

`||x||₁ = |x₁| + |x₂| + ... + |xₙ|`

### L2 norm

Take the square root of the sum of squared components:

`||x||₂ = √(x₁² + x₂² + ... + xₙ²)`

Here:

* `x` = the vector
* `x₁, x₂, ...` = its components
* `|x|` = absolute value, meaning distance from zero
* `||x||` = norm, meaning vector length/size

For distance between two vectors, subtract them first and then calculate their L2 norm:

`distance(a,b) = ||a-b||₂`

---

## Visual Example

For:

```text
v = [3, 4]
```

the vector forms a right triangle:

```text
y
↑
|          • (3,4)
|         /|
|        / |
|       /  | 4
|      /   |
|     /    |
|    /_____|
|      3
+----------------→ x
```

The L2 norm is the arrow's straight-line length:

```text
√(3² + 4²)
= √25
= 5
```

---

## Worked Examples

### Example 1 — L1 Norm

Given:

```text
x = [3, -4]
```

Take absolute values:

```text
|3| = 3
|-4| = 4
```

Add:

```text
||x||₁
= 3 + 4
= 7
```

**Answer: `7`**

---

### Example 2 — L2 Norm

Given:

```text
x = [3, 4]
```

Square each component:

```text
3² = 9
4² = 16
```

Add:

```text
9 + 16 = 25
```

Take the square root:

```text
√25 = 5
```

Therefore:

```text
||x||₂ = 5
```

---

### Example 3 — Compare L1 and L2

For:

```text
x = [3, 4]
```

L1:

```text
||x||₁ = 3 + 4 = 7
```

L2:

```text
||x||₂ = √(9 + 16) = 5
```

They measure size differently.

**Answer:**

```text
L1 = 7
L2 = 5
```

---

### Example 4 — Distance Between Vectors

Given:

```text
a = [1, 2]
b = [4, 6]
```

First subtract:

```text
a - b
= [1-4, 2-6]
= [-3, -4]
```

Now calculate its L2 norm:

```text
||a-b||₂
= √((-3)² + (-4)²)
= √(9 + 16)
= 5
```

Therefore the Euclidean distance between the vectors is:

```text
5
```

---

## Machine Learning Connection

Norms are used when ML algorithms need to measure **size, distance, or complexity**.

For example, suppose a model has weights:

```text
w = [3, 4]
```

Its L2 norm is:

```text
||w||₂ = 5
```

L2 norms are commonly used in **regularization**, where we discourage model weights from becoming unnecessarily large.

L2 distance is also useful when comparing vectors such as:

```text
embedding A = [1, 2]
embedding B = [4, 6]
```

Their distance is `5`.

---

## Exercises

### Easy

1. Calculate the L1 norm:

```text
[3, -2]
```

2. Calculate the L2 norm:

```text
[3, 4]
```

3. Calculate the L1 norm:

```text
[-5, 1, -2]
```

### Medium

4. Calculate the L2 norm:

```text
[6, 8]
```

5. Calculate the L1 and L2 norms of:

```text
[1, 2]
```

6. Find the L2 distance between:

```text
a = [1, 1]
b = [4, 5]
```

### Hard

7. Two vectors have the same L2 norm:

```text
a = [3, 4]
b = [0, 5]
```

Are their L2 norms equal? Calculate them.

8. Which vector has the larger L1 norm?

```text
a = [3, 3]
b = [5, 0]
```

---

## Expected Answers

1. Answer: `|3| + |-2| = 5`

2. Answer: `√(9+16) = 5`

3. Answer: `5 + 1 + 2 = 8`

4. Answer: `√(36+64) = 10`

5. Answer: L1 = `3`, L2 = `√5`

6. Answer: `[-3,-4] → √(9+16) = 5`

7. Answer: Yes. Both are `5`.

8. Answer: a > b

---

## What I Should Know Before Moving On

You are ready to continue if you can:

* Explain what a norm measures.
* Calculate an L1 norm.
* Calculate an L2 norm.
* Explain the geometric meaning of the L2 norm.
* Calculate the L2 distance between two vectors.
* Understand why ML algorithms care about vector size and distance.
* Distinguish between L1 and L2 norms.

---

# Topic: Linear Independence

## Description

Linear independence answers a simple question:

> **Do these vectors provide genuinely different directions/information, or can one be recreated from the others?**

The key idea is a **linear combination**.

A linear combination means multiplying vectors by numbers and adding them.

For example:

```text
2a + 3b
```

means:

1. multiply `a` by `2`
2. multiply `b` by `3`
3. add the results

Vectors are **linearly dependent** if at least one vector can be produced from the others.

For example:

```text
a = [1, 2]

b = [2, 4]
```

Notice:

```text
b = 2a
```

So `b` does not provide a new direction. It is just a scaled version of `a`.

Therefore `a` and `b` are **linearly dependent**.

If neither vector can be recreated from the other, they are **linearly independent**.

---

## Visual Example

Dependent vectors:

```text
          b = 2a
         ↗
        ↗
       ↗
      ↗ a
     /
----•----------------→
```

Both vectors point in exactly the same direction.

They do not provide two independent directions.

Independent vectors:

```text
       b
       ↑
       |
       |
       |
-------•--------→ a
```

The vectors point in different directions.

Together they provide two distinct directions.

---

## Worked Examples

### Example 1 — Obvious Dependence

Given:

```text
a = [1, 2]
b = [2, 4]
```

Ask whether one can be obtained by scaling the other.

```text
2a
= 2[1,2]
= [2,4]
= b
```

Therefore:

```text
b = 2a
```

So the vectors are **linearly dependent**.

---

### Example 2 — Obvious Independence

Given:

```text
a = [1, 0]
b = [0, 1]
```

Can we multiply `a` by one number to get `b`?

No.

```text
c[1,0] = [c,0]
```

The second component will always be `0`, so it can never become `[0,1]`.

Therefore these vectors are **linearly independent**.

They represent two different directions:

```text
a → right
b → up
```

---

### Example 3 — Three Vectors

Given:

```text
a = [1,0]
b = [0,1]
c = [2,3]
```

Can `c` be created from `a` and `b`?

Yes:

```text
2a + 3b

= 2[1,0] + 3[0,1]

= [2,0] + [0,3]

= [2,3]

= c
```

Therefore:

```text
a, b, c
```

are **linearly dependent**.

Why?

Because `c` does not introduce a new direction. It can already be constructed from `a` and `b`.

---

### Example 4 — Another Dependent Pair

Given:

```text
a = [3, -2]
b = [-6, 4]
```

Check whether one is a multiple of the other:

```text
-2a
= -2[3,-2]
= [-6,4]
= b
```

Therefore the vectors are **linearly dependent**.

---

## Machine Learning Connection

Suppose a dataset contains:

```text
feature 1 = number of kilometers
feature 2 = number of meters
```

These features contain essentially the same information because:

```text
meters = 1000 × kilometers
```

So one feature can be calculated directly from the other.

They are therefore **redundant**.

More generally, if features are linearly dependent, some information can be reconstructed from other features.

This can cause problems in some ML models, particularly linear models, because the model has redundant information rather than genuinely independent directions.

You do **not** need advanced linear algebra to use the basic idea:

> **Independent features add new information; dependent features contain information that can be constructed from other features.**

---

## Exercises

### Easy

1. Are these vectors dependent or independent?

```text
a = [1,2]
b = [2,4]
```

2. Are these vectors dependent or independent?

```text
a = [1,0]
b = [0,1]
```

3. Is this statement true?

```text
b = 3a
```

where:

```text
a = [2,1]
b = [6,3]
```

### Medium

4. Given:

```text
a = [1,0]
b = [0,1]
c = [3,5]
```

Can `c` be created using `a` and `b`?

5. Given:

```text
a = [2,3]
b = [4,6]
```

Find the number `k` such that:

```text
b = ka
```

6. Given:

```text
a = [1,2]
b = [2,1]
```

Can either vector be obtained by simply scaling the other?

### Hard

7. Given:

```text
a = [1,0]
b = [0,1]
c = [1,1]
```

Are these three vectors linearly independent?

Hint: Try constructing `c` using `a` and `b`.

8. Consider:

```text
a = [2,4]
b = [1,2]
```

Which vector contains the new direction, if any?

---

## Expected Answers

1. Answer: Dependent, because `b = 2a`.

2. Answer: Independent.

3. Answer: True; `[6,3] = 3[2,1]`.

4. Answer: Yes; `c = 3a + 5b`.

5. Answer: `k = 2`.

6. Answer: No. They are independent.

7. Answer: Dependent; `c = a + b`.

8. Answer: Neither provides a new direction relative to the other; `a = 2b`, so they are dependent.

---

## What I Should Know Before Moving On

You are ready to continue if you can:

* Explain what a linear combination is.
* Recognize when one vector is a scaled version of another.
* Explain linear dependence intuitively.
* Explain linear independence intuitively.
* Determine whether simple 2D vectors are dependent or independent.
* Recognize when one vector can be constructed from other vectors.
* Understand why redundant features can matter in ML.

---

# Overall Understanding

After these five topics, you should have the following mental model:

```text
VECTOR
  │
  ├── represents features / information
  │
  ├── add / subtract
  ├── scale
  └── dot product → weighted combination → one number
                    │
                    ↓
                 MATRIX
                    │
                    ├── stores many vectors
                    ├── rows / columns
                    └── matrix multiplication
                           │
                           ↓
                    applies many
                    weighted combinations
                           │
                           ↓
                      ML models
```

And:

```text
Vector
  │
  └── Norm → "How large is it?"
         │
         ├── L1 → add absolute values
         └── L2 → geometric length

Vectors
  │
  └── Linear independence
          │
          ├── Independent → genuinely different directions
          └── Dependent → some information can be constructed
                          from the others
```
