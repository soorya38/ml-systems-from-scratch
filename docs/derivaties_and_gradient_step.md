# Derivatives, Gradients & Gradient Descent

We will build this in exactly this order:

**Intuition → Function → Derivative → Partial Derivative → Gradient → Gradient direction → Loss → Negative Gradient → Learning Rate → Gradient Descent**

The goal is not to learn calculus. The goal is to understand **how an ML model knows which parameters to change and by how much**.

---

# 1. Functions

Before derivatives, we need one simple idea: a **function**.

A function takes an input and produces an output.

For example:

$$
f(x)=x^2
$$

Think of it as a machine:

```text
       input
         x
         │
         ▼
    ┌─────────┐
    │  f(x)=x² │
    └─────────┘
         │
         ▼
       output
```

If:

$$
x=2
$$

then:

$$
f(2)=2^2=4
$$

If:

$$
x=3
$$

then:

$$
f(3)=3^2=9
$$

So:

```text
x       f(x)
────────────
-2       4
-1       1
 0       0
 1       1
 2       4
 3       9
```

The function describes a relationship between the input and output.

---

# 2. What Is a Derivative?

Now imagine changing the input slightly.

For:

$$
f(x)=x^2
$$

suppose we move from:

$$
x=2
$$

to:

$$
x=2.1
$$

The output changes from:

$$
f(2)=4
$$

to:

$$
f(2.1)=4.41
$$

So the question is:

> **How quickly does the output change when I change the input?**

That is what the **derivative** tells us.

### Core idea

> **A derivative tells us how the output of a function changes when its input changes slightly.**

For a graph, the derivative tells us the **slope** at a particular point.

---

# 3. Derivative = Slope

Consider:

```text
y
│
│              /
│            /
│          /
│        /
│      /
│    /
│  /
└──────────────── x
```

A line going upward has a **positive slope**.

Therefore its derivative is positive.

Now:

```text
y
│\
│ \
│  \
│   \
│    \
│     \
└──────────────── x
```

This line goes downward.

Its slope is negative.

Therefore its derivative is negative.

And a flat line:

```text
y
│
│──────────────
│
└──────────────── x
```

has zero slope.

Therefore its derivative is zero.

So:

| Derivative | Meaning                  |
| ---------- | ------------------------ |
| Positive   | Function is increasing   |
| Negative   | Function is decreasing   |
| Zero       | Function is locally flat |

This sign will become **extremely important for gradient descent**.

---

# 4. Derivative of (x^2)

Consider:

$$
f(x)=x^2
$$

Its derivative is:

$$
f'(x)=2x
$$

Don't worry about where this formula comes from yet. For now, learn how to **use** it.

Let's evaluate it at different points.

### At (x=2)

$$
f'(2)=2(2)=4
$$

So the slope is:

$$
\boxed{4}
$$

That means around (x=2), increasing (x) makes the function increase.

---

### At (x=-3)

$$
f'(-3)=2(-3)=-6
$$

So the slope is:

$$
\boxed{-6}
$$

The negative sign means the function is decreasing as (x) increases around that point.

---

### At (x=0)

$$
f'(0)=2(0)=0
$$

So the slope is:

$$
\boxed{0}
$$

The function is flat at the bottom.

---

# 5. Why Does (x^2) Have Negative Derivatives on the Left?

Look at:

$$
f(x)=x^2
$$

Its shape is:

```text
       y
       │
     \ │ /
      \│/
       ●
      / \
     /   \
─────┼──────── x
    -      +
```

More accurately:

```text
             y
             │
        \         /
         \       /
          \     /
           \   /
            \_/
             ●
─────────────┼──────────── x
            0
```

On the **left side**, the curve slopes downward as we move from left to right.

Therefore:

$$
f'(x)<0
$$

when:

$$
x<0
$$

At the bottom:

$$
f'(0)=0
$$

On the **right side**, the curve slopes upward.

Therefore:

$$
f'(x)>0
$$

when:

$$
x>0
$$

So:

```text
x < 0       x = 0       x > 0
  │            │            │
  ▼            ▼            ▼
negative      zero       positive
derivative  derivative   derivative
```

This is the first major idea we will use for gradient descent.

---

# 6. Derivative Notation

You will see several ways to write a derivative.

If:

$$
y=f(x)
$$

we can write:

$$
f'(x)
$$

or:

$$
\frac{dy}{dx}
$$

They mean essentially the same thing here:

> **How quickly does (y) change when (x) changes?**

For example:

$$
f(x)=x^2
$$

means:

$$
f'(x)=2x
$$

or, if (y=x^2):

$$
\frac{dy}{dx}=2x
$$

---

# 7. Basic Derivative Rules

We only need a few rules for now.

## Rule 1: Derivative of a constant

A constant doesn't change.

For example:

$$
f(x)=5
$$

Its graph is flat:

```text
y
│
│──────────── 5
│
└──────────────── x
```

Therefore:

$$
\boxed{\frac{d}{dx}(5)=0}
$$

---

## Rule 2: Derivative of (x)

$$
f(x)=x
$$

The slope is always 1.

Therefore:

$$
\boxed{\frac{d}{dx}(x)=1}
$$

---

## Rule 3: Derivative of (x^2)

$$
\boxed{\frac{d}{dx}(x^2)=2x}
$$

---

## Rule 4: Power rule

For the simple powers we'll use:

$$
\boxed{\frac{d}{dx}(x^n)=nx^{n-1}}
$$

For example:

$$
\frac{d}{dx}(x^3)
=

3x^2
$$

And:

$$
\frac{d}{dx}(x^4)
=

4x^3
$$

You don't need more differentiation techniques yet.

---

# 8. Derivative of a Simple Polynomial

Consider:

$$
f(x)=x^2+3x+5
$$

Differentiate each term:

$$
\frac{d}{dx}(x^2)=2x
$$

$$
\frac{d}{dx}(3x)=3
$$

$$
\frac{d}{dx}(5)=0
$$

Therefore:

$$
\boxed{f'(x)=2x+3}
$$

### At (x=2)

$$
f'(2)=2(2)+3
$$

$$
=4+3
$$

$$
\boxed{7}
$$

So the slope at (x=2) is 7.

---

# 9. Worked Examples

## Example 1

$$
f(x)=x^2
$$

Derivative:

$$
f'(x)=2x
$$

At (x=2):

$$
f'(2)=4
$$

**Meaning:** the function is increasing at that point, with slope 4.

---

## Example 2

$$
f(x)=x^2
$$

At:

$$
x=-3
$$

we get:

$$
f'(-3)=2(-3)
$$

$$
=-6
$$

**Meaning:** the function is decreasing as (x) increases around (x=-3).

---

## Example 3

$$
f(x)=3x^2+2x+7
$$

Differentiate:

$$
\frac{d}{dx}(3x^2)=6x
$$

$$
\frac{d}{dx}(2x)=2
$$

$$
\frac{d}{dx}(7)=0
$$

Therefore:

$$
\boxed{f'(x)=6x+2}
$$

At (x=1):

$$
f'(1)=6(1)+2=8
$$

So the slope is:

$$
\boxed{8}
$$

---

# 10. The Important ML Interpretation

Forget calculus for a moment.

Suppose:

$$
L(w)
$$

is a **loss function**.

Here:

* (w) = model parameter
* (L(w)) = loss produced by that parameter

For example:

$$
L(w)=w^2
$$

Suppose:

$$
w=4
$$

Then:

$$
L(4)=16
$$

The derivative is:

$$
L'(w)=2w
$$

Therefore:

$$
L'(4)=8
$$

What does **8** tell us?

It tells us:

> If we change (w) slightly, the loss is currently increasing with (w), with a local slope of 8.

So the derivative gives the model useful information:

```text
Parameter changes
       │
       ▼
How does loss change?
       │
       ▼
   derivative
```

This is why derivatives are useful in ML.

---

# 11. Why One Derivative Isn't Enough

So far we have:

$$
L(w)
$$

with one parameter.

But a real ML model can have many parameters:

$$
w_1,w_2,w_3,\ldots
$$

For example:

$$
L(w_1,w_2)
$$

Now we have two inputs.

We need to ask two different questions:

> How does the loss change if I change (w_1)?

and:

> How does the loss change if I change (w_2)?

This leads us to **partial derivatives**.

---

# 12. Partial Derivatives

Consider:

$$
f(x,y)=x^2+y^2
$$

There are two inputs:

```text
x ──┐
    ├──► f(x,y)
y ──┘
```

We can calculate the effect of changing (x) while keeping (y) fixed.

That is:

$$
\frac{\partial f}{\partial x}
$$

The symbol:

$$
\partial
$$

means we're taking a **partial derivative**.

For:

$$
f(x,y)=x^2+y^2
$$

with respect to (x):

$$
\frac{\partial f}{\partial x}=2x
$$

Why does (y^2) disappear?

Because when calculating the change with respect to (x), we treat (y) as fixed.

Similarly:

$$
\frac{\partial f}{\partial y}=2y
$$

So:

$$
\boxed{
\frac{\partial f}{\partial x}=2x
}
$$

and:

$$
\boxed{
\frac{\partial f}{\partial y}=2y
}
$$

---

# 13. What Is a Gradient?

We now collect all the partial derivatives together.

For:

$$
f(x,y)
$$

the gradient is:

$$
\boxed{
\nabla f(x,y)=
\begin{bmatrix}
\frac{\partial f}{\partial x}\
\frac{\partial f}{\partial y}
\end{bmatrix}
}
$$

Let's decode this.

$$
\nabla
$$

This symbol means **gradient**.

### (f)

The function we're differentiating.

### The two entries

$$
\frac{\partial f}{\partial x}
$$

and

$$
\frac{\partial f}{\partial y}
$$

are the slopes with respect to (x) and (y).

So the gradient is simply:

> **All the partial derivatives collected into one vector.**

---

# 14. Gradient Example

Consider:

$$
f(x,y)=x^2+y^2
$$

We already calculated:

$$
\frac{\partial f}{\partial x}=2x
$$

$$
\frac{\partial f}{\partial y}=2y
$$

Therefore:

$$
\nabla f(x,y)
=

\begin{bmatrix}
2x\
2y
\end{bmatrix}
$$

Now evaluate at:

$$
(x,y)=(1,2)
$$

First:

$$
\frac{\partial f}{\partial x}=2(1)=2
$$

Second:

$$
\frac{\partial f}{\partial y}=2(2)=4
$$

Therefore:

$$
\boxed{
\nabla f(1,2)=
\begin{bmatrix}
2\
4
\end{bmatrix}
}
$$

---

# 15. What Does [2, 4] Mean?

This is important.

The gradient:

$$
[2,4]
$$

contains two pieces of information:

```text
[ 2 , 4 ]
  │   │
  │   └── slope with respect to y
  └────── slope with respect to x
```

So:

* changing (x) affects the function with slope 2
* changing (y) affects the function with slope 4

The gradient therefore tells us how the function is changing with respect to **all its inputs**.

---

# 16. Derivative vs Partial Derivative vs Gradient

Keep this distinction clear:

### One input

$$
f(x)
$$

→ derivative:

$$
f'(x)
$$

### Multiple inputs

$$
f(x,y)
$$

→ partial derivatives:

$$
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y}
$$

→ collect them:

$$
\nabla f
$$

So:

```text
One variable
     │
     ▼
 derivative
     │
     ▼
     slope


Multiple variables
     │
     ▼
partial derivatives
     │
     ▼
   gradient
     │
     ▼
slopes in all
input directions
```

---

# 17. Which Direction Does the Gradient Point?

This is the key idea.

The gradient points in the direction where the function increases **most rapidly locally**.

For:

$$
f(x,y)=x^2+y^2
$$

at:

$$
(1,2)
$$

we found:

$$
\nabla f=[2,4]
$$

So the function is locally increasing most strongly in the direction:

$$
[2,4]
$$

You can visualize the function as a bowl:

```text
             higher
          __________
        /            \
       /              \
      /                \
     /        ●         \
    /         │          \
   /          │           \
  /___________┴____________\
              minimum
```

The gradient points **uphill**.

Therefore:

> **Gradient → direction of greatest local increase.**

And consequently:

> **Negative gradient → direction of greatest local decrease.**

This is exactly what we need for ML.

---

# 18. Why ML Wants the Negative Gradient

An ML model usually wants to **minimize loss**.

Suppose:

$$
L(w)
$$

represents the loss.

We don't want:

```text
HIGH LOSS
         │
         │
         V
LOW LOSS
```

We want to move toward lower loss.

But the gradient tells us the direction of **increasing** loss.

Therefore we go in the opposite direction.

```text
             gradient
                ↑
                │
                │
          ●─────┘
         /
        /
       ↓
 negative gradient
```

Hence:

$$
\boxed{\text{gradient} \rightarrow \text{increase}}
$$

$$
\boxed{-\text{gradient} \rightarrow \text{decrease}}
$$

This is why gradient descent uses a minus sign.

---

# 19. Gradient Descent

Now we can finally define gradient descent.

The problem is:

> We have a loss function. We want to find parameter values that make the loss smaller.

Gradient descent repeatedly does this:

```text
1. Calculate gradient
        ↓
2. Look at its direction
        ↓
3. Move opposite to it
        ↓
4. Repeat
```

The update rule is:

$$
\boxed{w_{\text{new}} = w_{\text{old}} - \eta \nabla L(w)}
$$

This formula is extremely important.

Let's understand **every part**.

---

# 20. Understanding the Update Formula

$$
\boxed{w_{\text{new}} = w_{\text{old}} - \eta \nabla L(w)}
$$

$$
(w_{\text{old}})
$$

The current parameter.

Example:

$$
w_{\text{old}}=4
$$

---

### (L(w))

The loss function.

It tells us how bad the model currently is.

---

$$
(\nabla L(w))
$$

The gradient of the loss.

It tells us:

> **Which direction makes the loss increase, and how strongly.**

For one parameter, this is simply the derivative.

---

$$
(\eta)
$$

This is called the **learning rate**.

It controls the size of our step.

---

### Minus sign

The gradient points toward increasing loss.

We want decreasing loss.

Therefore:

$$
-\nabla L(w)
$$

points in the opposite direction.

---

# 21. The Most Important Interpretation

Remember these two statements:

> **THE GRADIENT TELLS US THE DIRECTION.**

> **THE LEARNING RATE TELLS US HOW BIG THE STEP IS.**

That is the heart of gradient descent.

---

# 22. Gradient Descent Example 1

Consider:

$$
L(w)=w^2
$$

We want to minimize this.

Obviously the minimum is at:

$$
w=0
$$

But let's pretend we don't know that and use gradient descent.

Start with:

$$
w=4
$$

Learning rate:

$$
\eta=0.1
$$

### Step 1: Calculate derivative

$$
L'(w)=2w
$$

At (w=4):

$$
L'(4)=8
$$

So:

$$
\text{gradient}=8
$$

The gradient is positive.

Therefore, increasing (w) increases the loss.

To reduce the loss, we should decrease (w).

---

### Step 2: Apply update

$$
w_{\text{new}}
=
w_{\text{old}}-\eta L'(w)
$$

Substitute:

$$
w_{\text{new}}
=
4-0.1(8)
$$

$$
=4-0.8
$$

$$
\boxed{w_{\text{new}}=3.2}
$$

We moved:

$$
4\rightarrow3.2
$$

---

# 23. Another Update

Now:

$$
w=3.2
$$

Calculate the derivative:

$$
L'(3.2)=2(3.2)=6.4
$$

Update:

$$
w_{\text{new}}
=
3.2-0.1(6.4)
$$

$$
=3.2-0.64
$$

$$
\boxed{w_{\text{new}}=2.56}
$$

So:

```text
4
│
└──► 3.2
       │
       └──► 2.56
```

Another update:

$$
L'(2.56)=5.12
$$

Therefore:

$$
w_{\text{new}}
=
2.56-0.1(5.12)
$$

$$
=2.56-0.512
$$

$$
\boxed{2.048}
$$

So:

```text
4 → 3.2 → 2.56 → 2.048 → ...
```

We are approaching:

$$
0
$$

---

# 24. Why Does It Work?

Look at the function:

$$
L(w)=w^2
$$

```text
Loss
  │
  │ \             /
  │  \           /
  │   \         /
  │    \       /
  │     \_____/
  │         ●
  └────────────────── w
            0
```

Starting at:

$$
w=4
$$

we are on the right side.

The slope is positive.

Therefore gradient descent moves **left**.

```text
                  ●
                 /
                /
               ↓
              /
             /
       ______●______
             0
```

Each update gets us closer to the bottom.

---

# 25. Starting From a Negative Value

Now start at:

$$
w=-4
$$

Again:

$$
L(w)=w^2
$$

Derivative:

$$
L'(w)=2w
$$

Therefore:

$$
L'(-4)=2(-4)=-8
$$

The gradient is negative.

Now perform the update:

$$
w_{\text{new}}
=
-4-0.1(-8)
$$

Notice the two minus signs:

$$
=-4+0.8
$$

$$
\boxed{-3.2}
$$

So:

$$
-4\rightarrow-3.2
$$

We're moving **right**, toward zero.

This is why the minus sign in the formula works automatically.

```text
-4  →  -3.2  →  -2.56  →  ...
                    →
                   0
```

The gradient was negative, so:

$$
-\text{negative}=\text{positive}
$$

and the parameter increases.

---

# 26. The Sign of the Gradient Controls Direction

For:

$$
L(w)=w^2
$$

### If (w>0)

$$
L'(w)>0
$$

Update:

$$
w_{\text{new}}=w-\text{positive}
$$

Therefore (w) decreases.

---

### If (w<0)

$$
L'(w)<0
$$

Update:

$$
w_{\text{new}}=w-\text{negative}
$$

Therefore (w) increases.

---

### If (w=0)

$$
L'(0)=0
$$

Update:

$$
w_{\text{new}}=w
$$

Nothing changes.

So:

```text
             w < 0       w = 0       w > 0
                │           │            │
                ▼           ▼            ▼
            gradient      gradient    gradient
             negative       zero       positive
                │           │            │
                ▼           ▼            ▼
            move right    stay       move left
```

---

# 27. Multiple Parameters

Now consider:

$$
L(w_1,w_2)=w_1^2+w_2^2
$$

There are two parameters:

$$
w_1
$$

and:

$$
w_2
$$

The gradient is:

$$
\nabla L=
\begin{bmatrix}
2w_1\
2w_2
\end{bmatrix}
$$

Start with:

$$
w=
\begin{bmatrix}
2\
3
\end{bmatrix}
$$

and:

$$
\eta=0.1
$$

---

## Step 1: Calculate the gradient

First component:

$$
2w_1=2(2)=4
$$

Second component:

$$
2w_2=2(3)=6
$$

Therefore:

$$
\nabla L=
\begin{bmatrix}
4\
6
\end{bmatrix}
$$

---

## Step 2: Apply gradient descent

$$
w_{\text{new}} = w_{\text{old}} - \eta \nabla L
$$

Substitute:

$$
\begin{bmatrix}
w_1\
w_2
\end{bmatrix}_{new}
=
\begin{bmatrix}
2\
3
\end{bmatrix}
-
0.1
\begin{bmatrix}
4\
6
\end{bmatrix}
$$

Multiply:

$$
0.1
\begin{bmatrix}
4\
6
\end{bmatrix}
=
\begin{bmatrix}
0.4\
0.6
\end{bmatrix}
$$

Therefore:

$$
w_{\text{new}}
=
\begin{bmatrix}
2\
3
\end{bmatrix}
-
\begin{bmatrix}
0.4\
0.6
\end{bmatrix}
$$

So:

$$
\boxed{
w_{\text{new}}
=
\begin{bmatrix}
1.6\
2.4
\end{bmatrix}
}
$$

Both parameters changed simultaneously:

$$
w_1:2\rightarrow1.6
$$

$$
w_2:3\rightarrow2.4
$$

That's what happens in a real ML model too.

A model may have thousands or millions of parameters, and gradient descent calculates how each one should change.

---

# 28. Learning Rate

The learning rate is:

$$
\eta
$$

It controls **how large a step we take**.

Consider:

$$
L(w)=w^2
$$

at:

$$
w=4
$$

The gradient is:

$$
8
$$

### Small learning rate

Suppose:

$$
\eta=0.01
$$

Then:

$$
w_{\text{new}}
=
4-0.01(8)
$$

$$
=3.92
$$

Tiny movement.

---

### Reasonable learning rate

$$
\eta=0.1
$$

gives:

$$
w_{\text{new}}=3.2
$$

Larger movement.

---

### Very large learning rate

Suppose:

$$
\eta=1
$$

Then:

$$
w_{\text{new}}
=
4-1(8)
$$

$$
=-4
$$

We jumped from one side of the minimum to the other.

A sufficiently large learning rate can cause repeated overshooting and unstable behavior.

So:

```text
Learning rate
     │
     ├── too small ──► very slow
     │
     ├── reasonable ─► useful progress
     │
     └── too large ──► overshooting / instability
```

---

# 29. The Complete Picture

We can now connect everything.

Suppose an ML model has parameters:

$$
w
$$

and loss:

$$
L(w)
$$

The model asks:

> "How does my loss change if I change my parameter?"

Derivative/gradient answers that.

Then:

> "Which direction should I move to reduce the loss?"

Negative gradient answers that.

Then:

> "How far should I move?"

Learning rate answers that.

So:

$$
\boxed{w_{\text{new}} = w_{\text{old}} - \eta \nabla L(w)}
$$

means:

```text
Current parameters
        │
        ▼
 Calculate gradient
        │
        ▼
Which direction
increases loss?
        │
        ▼
Go in the opposite direction
        │
        ▼
Learning rate determines
how far
        │
        ▼
New parameters
        │
        ▼
Calculate loss again
        │
        ▼
Repeat
```

This is the fundamental idea behind gradient-based ML training.

---

# Exercises

## Easy

### 1. Derivative

Find the derivative:

$$
f(x)=x^2
$$

---

### 2. Linear Function

Find:

$$
f'(x)
$$

for:

$$
f(x)=5x+3
$$

---

### 3. Constant Derivative

Find:

$$
f'(x)
$$

for:

$$
f(x)=10
$$

---

### 4. Evaluate a Derivative

Given:

$$
f(x)=x^2
$$

calculate:

$$
f'(4)
$$

---

### 5. Determine the Sign

For:

$$
f(x)=x^2
$$

is the derivative positive, negative, or zero at:

$$
x=-5
$$

---

### 6. Polynomial Derivative

Find:

$$
f'(x)
$$

for:

$$
f(x)=3x^2+4x+7
$$

---

### 7. Evaluate a Polynomial Derivative

Given:

$$
f(x)=3x^2+4x+7
$$

calculate:

$$
f'(-2)
$$

---

### 8. Basic Power Rule

Find:

$$
f'(x)
$$

for:

$$
f(x)=x^3
$$

---

### 9. Identify the Direction

Given:

$$
f'(x)=-7
$$

is the function increasing or decreasing at that point?

---

### 10. Zero Derivative

For:

$$
f(x)=x^2
$$

find the value of $x$ where:

$$
f'(x)=0
$$

---

# Medium

### 11. Partial Derivative

Given:

$$
f(x,y)=x^2+y^2
$$

calculate:

$$
\frac{\partial f}{\partial x}
$$

and:

$$
\frac{\partial f}{\partial y}
$$

---

### 12. Gradient

Given:

$$
f(x,y)=x^2+y^2
$$

find:

$$
\nabla f(x,y)
$$

---

### 13. Evaluate the Gradient

For:

$$
f(x,y)=x^2+y^2
$$

calculate the gradient at:

$$
(x,y)=(2,3)
$$

---

### 14. Partial Derivative with Cross Term

Given:

$$
f(x,y)=3x^2+4xy+5y^2
$$

calculate:

$$
\frac{\partial f}{\partial x}
$$

---

### 15. Second Partial Derivative

For:

$$
f(x,y)=3x^2+4xy+5y^2
$$

calculate:

$$
\frac{\partial f}{\partial y}
$$

---

### 16. Complete Gradient

Given:

$$
f(x,y)=3x^2+4xy+5y^2
$$

find:

$$
\nabla f(x,y)
$$

---

### 17. Evaluate a Gradient

Given:

$$
f(x,y)=3x^2+4xy+5y^2
$$

calculate:

$$
\nabla f(1,2)
$$

---

### 18. Interpret a Gradient

Suppose:

$$
\nabla L(w_1,w_2)=
\begin{bmatrix}
4\\
-3
\end{bmatrix}
$$

Answer:

1. What does the $4$ tell you about $w_1$?
2. What does the $-3$ tell you about $w_2$?
3. Should gradient descent increase or decrease $w_1$?
4. Should gradient descent increase or decrease $w_2$?

---

### 19. Three Parameters

Given:

$$
f(x,y,z)=x^2+y^2+z^2
$$

find:

$$
\nabla f(x,y,z)
$$

---

### 20. Evaluate a Three-Parameter Gradient

For:

$$
f(x,y,z)=x^2+y^2+z^2
$$

calculate the gradient at:

$$
(x,y,z)=(1,-2,3)
$$

---

# Hard — Gradient Descent

### 21. One Gradient Descent Update

Given:

$$
L(w)=w^2
$$

Start with:

$$
w=5
$$

and:

$$
\eta=0.1
$$

Calculate:

1. $L'(w)$
2. The gradient at $w=5$
3. The new value of $w$

---

### 22. Multiple Gradient Descent Updates

Given:

$$
L(w)=w^2
$$

Start with:

$$
w=8
$$

and:

$$
\eta=0.1
$$

Perform **four gradient descent updates**.

Show:

$$
w_0\rightarrow w_1\rightarrow w_2\rightarrow w_3\rightarrow w_4
$$

---

### 23. Gradient Descent from a Negative Starting Point

Given:

$$
L(w)=w^2
$$

Start with:

$$
w=-6
$$

and:

$$
\eta=0.1
$$

Perform **three updates**.

Explain why $w$ increases even though the update rule subtracts the gradient.

---

### 24. Different Learning Rates

Given:

$$
L(w)=w^2
$$

Start with:

$$
w=5
$$

Calculate one gradient descent update for each learning rate:

#### a.

$$
\eta=0.01
$$

#### b.

$$
\eta=0.1
$$

#### c.

$$
\eta=0.5
$$

Which learning rate produces the largest parameter update?

---

### 25. Two-Parameter Gradient Descent

Given:

$$
L(w_1,w_2)=w_1^2+w_2^2
$$

Start with:

$$
w=
\begin{bmatrix}
3\\
4
\end{bmatrix}
$$

and:

$$
\eta=0.1
$$

Calculate:

1. $\frac{\partial L}{\partial w_1}$
2. $\frac{\partial L}{\partial w_2}$
3. The gradient
4. The updated $w_1$
5. The updated $w_2$
6. The new parameter vector

---

### 26. Two Gradient Descent Updates

Given:

$$
L(w_1,w_2)=w_1^2+w_2^2
$$

Start with:

$$
w=
\begin{bmatrix}
4\\
2
\end{bmatrix}
$$

and:

$$
\eta=0.1
$$

Perform **two complete gradient descent updates**.

Show:

$$
w_0\rightarrow w_1\rightarrow w_2
$$

Also calculate the loss:

- before any updates
- after the first update
- after the second update

---

### 27. Unequal Parameter Effects

Given:

$$
L(w_1,w_2)=2w_1^2+w_2^2
$$

Start with:

$$
w_1=3,\qquad w_2=4
$$

and:

$$
\eta=0.1
$$

Calculate:

1. $\frac{\partial L}{\partial w_1}$
2. $\frac{\partial L}{\partial w_2}$
3. The gradient
4. One gradient descent update
5. The loss before the update
6. The loss after the update
7. Verify that the loss decreased

---

### 28. Three-Parameter Gradient Descent

Given:

$$
L(w_1,w_2,w_3)=w_1^2+w_2^2+w_3^2
$$

Start with:

$$
w=
\begin{bmatrix}
2\\
-3\\
4
\end{bmatrix}
$$

and:

$$
\eta=0.1
$$

Calculate:

1. The gradient
2. The negative gradient
3. One gradient descent update
4. The new parameter vector
5. The loss before and after the update

---

### 29. Reason About the Gradient

Suppose the current parameters are:

$$
w=
\begin{bmatrix}
2\\
-3
\end{bmatrix}
$$

and the gradient is:

$$
\nabla L=
\begin{bmatrix}
-4\\
6
\end{bmatrix}
$$

with:

$$
\eta=0.1
$$

Calculate:

1. The negative gradient
2. The update amount for each parameter
3. The new parameter vector
4. Does $w_1$ increase or decrease?
5. Does $w_2$ increase or decrease?

---

### 30. Complete Gradient Descent Problem

Consider the loss function:

$$
L(w_1,w_2)=w_1^2+2w_2^2
$$

Start with:

$$
w_1=-3,\qquad w_2=4
$$

and:

$$
\eta=0.1
$$

Perform **three gradient descent updates**.

For each update, calculate:

1. The current gradient
2. The update for $w_1$
3. The update for $w_2$
4. The new values of $w_1,w_2$
5. The loss after the update

Finally answer:

- Is the loss decreasing?
- Are the parameters moving toward the minimum?
- What is the role of the negative sign in the update?
- What would happen if the learning rate were much larger?

---

# Expected Answers

## Easy

### 1. Answer

$$
f'(x)=2x
$$

### 2. Answer

$$
f'(x)=5
$$

### 3. Answer

$$
f'(x)=0
$$

### 4. Answer

$$
f'(x)=2x
$$

$$
f'(4)=8
$$

### 5. Answer

**Negative.**

$$
f'(-5)=-10
$$

### 6. Answer

$$
f'(x)=6x+4
$$

### 7. Answer

$$
f'(-2)=6(-2)+4
$$

$$
=-8
$$

### 8. Answer

$$
f'(x)=3x^2
$$

### 9. Answer

**Decreasing.**

### 10. Answer

$$
f'(x)=2x
$$

$$
2x=0
$$

$$
\boxed{x=0}
$$

---

# Medium

### 11. Answer

$$
\frac{\partial f}{\partial x}=2x
$$

$$
\frac{\partial f}{\partial y}=2y
$$

### 12. Answer

$$
\boxed{
\nabla f=
\begin{bmatrix}
2x\\
2y
\end{bmatrix}}
$$

### 13. Answer

$$
\nabla f(2,3)=
\begin{bmatrix}
4\\
6
\end{bmatrix}
$$

### 14. Answer

$$
\boxed{
\frac{\partial f}{\partial x}=6x+4y
}
$$

### 15. Answer

$$
\boxed{
\frac{\partial f}{\partial y}=4x+10y
}
$$

### 16. Answer

$$
\boxed{
\nabla f=
\begin{bmatrix}
6x+4y\\
4x+10y
\end{bmatrix}}
$$

### 17. Answer

At $(1,2)$:

$$
\frac{\partial f}{\partial x}=6(1)+4(2)=14
$$

$$
\frac{\partial f}{\partial y}=4(1)+10(2)=24
$$

Therefore:

$$
\boxed{
\nabla f(1,2)=
\begin{bmatrix}
14\\
24
\end{bmatrix}}
$$

### 18. Answer

Given:

$$
\nabla L=
\begin{bmatrix}
4\\
-3
\end{bmatrix}
$$

1. $w_1$: increasing $w_1$ increases the loss.
2. $w_2$: increasing $w_2$ decreases the loss.
3. Gradient descent decreases $w_1$.
4. Gradient descent increases $w_2$.

### 19. Answer

$$
\boxed{
\nabla f=
\begin{bmatrix}
2x\\
2y\\
2z
\end{bmatrix}}
$$

### 20. Answer

At $(1,-2,3)$:

$$
\boxed{
\nabla f=
\begin{bmatrix}
2\\
-4\\
6
\end{bmatrix}}
$$

---

# Hard — Gradient Descent

### 21. Answer

$$
L'(w)=2w
$$

$$
L'(5)=10
$$

$$
w_{\text{new}}
=
5-0.1(10)
$$

$$
\boxed{w_{\text{new}}=4}
$$

---

### 22. Answer

$$
w_0=8
$$

Update 1:

$$
w_1=8-0.1(16)=6.4
$$

Update 2:

$$
w_2=6.4-0.1(12.8)=5.12
$$

Update 3:

$$
w_3=5.12-0.1(10.24)=4.096
$$

Update 4:

$$
w_4=4.096-0.1(8.192)=3.2768
$$

Therefore:

$$
\boxed{
8\rightarrow6.4\rightarrow5.12\rightarrow4.096\rightarrow3.2768
}
$$

---

### 23. Answer

$$
L'(w)=2w
$$

Start:

$$
w=-6
$$

Update 1:

$$
w=-6-0.1(-12)=-4.8
$$

Update 2:

$$
w=-4.8-0.1(-9.6)=-3.84
$$

Update 3:

$$
w=-3.84-0.1(-7.68)=-3.072
$$

Therefore:

$$
\boxed{
-6\rightarrow-4.8\rightarrow-3.84\rightarrow-3.072
}
$$

The gradient is negative, so subtracting the negative gradient increases $w$.

---

### 24. Answer

At:

$$
w=5
$$

the gradient is:

$$
L'(5)=10
$$

#### a. $\eta=0.01$

$$
w_{\text{new}}=5-0.01(10)
$$

$$
\boxed{4.9}
$$

#### b. $\eta=0.1$

$$
w_{\text{new}}=5-0.1(10)
$$

$$
\boxed{4}
$$

#### c. $\eta=0.5$

$$
w_{\text{new}}=5-0.5(10)
$$

$$
\boxed{0}
$$

Largest step:

$$
\boxed{\eta=0.5}
$$

---

### 25. Answer

$$
L(w_1,w_2)=w_1^2+w_2^2
$$

Partial derivatives:

$$
\frac{\partial L}{\partial w_1}=2w_1
$$

$$
\frac{\partial L}{\partial w_2}=2w_2
$$

At $(3,4)$:

$$
\nabla L=
\begin{bmatrix}
6\\
8
\end{bmatrix}
$$

Update:

$$
\begin{bmatrix}
3\\
4
\end{bmatrix}
-
0.1
\begin{bmatrix}
6\\
8
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
2.4\\
3.2
\end{bmatrix}
$$

Therefore:

$$
\boxed{
w_{\text{new}}=
\begin{bmatrix}
2.4\\
3.2
\end{bmatrix}}
$$

---

### 26. Answer

Start:

$$
w_0=
\begin{bmatrix}
4\\
2
\end{bmatrix}
$$

Gradient:

$$
\nabla L=
\begin{bmatrix}
2w_1\\
2w_2
\end{bmatrix}
$$

First update:

$$
\nabla L=
\begin{bmatrix}
8\\
4
\end{bmatrix}
$$

$$
w_1=
\begin{bmatrix}
4\\
2
\end{bmatrix}
-
0.1
\begin{bmatrix}
8\\
4
\end{bmatrix}
$$

$$
\boxed{
w_1=
\begin{bmatrix}
3.2\\
1.6
\end{bmatrix}}
$$

Second update:

$$
\nabla L=
\begin{bmatrix}
6.4\\
3.2
\end{bmatrix}
$$

$$
w_2=
\begin{bmatrix}
3.2\\
1.6
\end{bmatrix}
-
0.1
\begin{bmatrix}
6.4\\
3.2
\end{bmatrix}
$$

$$
\boxed{
w_2=
\begin{bmatrix}
2.56\\
1.28
\end{bmatrix}}
$$

Losses:

$$
L(4,2)=20
$$

$$
L(3.2,1.6)=12.8
$$

$$
L(2.56,1.28)=8.192
$$

The loss decreases at every update.

---

### 27. Answer

$$
L(w_1,w_2)=2w_1^2+w_2^2
$$

Partial derivatives:

$$
\frac{\partial L}{\partial w_1}=4w_1
$$

$$
\frac{\partial L}{\partial w_2}=2w_2
$$

At $(3,4)$:

$$
\nabla L=
\begin{bmatrix}
12\\
8
\end{bmatrix}
$$

Update:

$$
\begin{bmatrix}
3\\
4
\end{bmatrix}
-
0.1
\begin{bmatrix}
12\\
8
\end{bmatrix}
=
\begin{bmatrix}
1.8\\
3.2
\end{bmatrix}
$$

Loss before:

$$
L(3,4)=2(3^2)+4^2
$$

$$
=34
$$

Loss after:

$$
L(1.8,3.2)
=
2(1.8^2)+3.2^2
$$

$$
=16.72
$$

Therefore:

$$
\boxed{34\rightarrow16.72}
$$

The loss decreased.

---

### 28. Answer

$$
L(w_1,w_2,w_3)=w_1^2+w_2^2+w_3^2
$$

Gradient:

$$
\nabla L=
\begin{bmatrix}
2w_1\\
2w_2\\
2w_3
\end{bmatrix}
$$

At $(2,-3,4)$:

$$
\nabla L=
\begin{bmatrix}
4\\
-6\\
8
\end{bmatrix}
$$

Negative gradient:

$$
-\nabla L=
\begin{bmatrix}
-4\\
6\\
-8
\end{bmatrix}
$$

Update:

$$
\begin{bmatrix}
2\\
-3\\
4
\end{bmatrix}
-
0.1
\begin{bmatrix}
4\\
-6\\
8
\end{bmatrix}
$$

$$
=
\boxed{
\begin{bmatrix}
1.6\\
-2.4\\
3.2
\end{bmatrix}}
$$

Loss before:

$$
L(2,-3,4)=29
$$

Loss after:

$$
L(1.6,-2.4,3.2)=18.56
$$

---

### 29. Answer

Given:

$$
\nabla L=
\begin{bmatrix}
-4\\
6
\end{bmatrix}
$$

Negative gradient:

$$
-\nabla L=
\begin{bmatrix}
4\\
-6
\end{bmatrix}
$$

Update amount:

$$
0.1
\begin{bmatrix}
4\\
-6
\end{bmatrix}
=
\begin{bmatrix}
0.4\\
-0.6
\end{bmatrix}
$$

New parameters:

$$
\begin{bmatrix}
2\\
-3
\end{bmatrix}
+
\begin{bmatrix}
0.4\\
-0.6
\end{bmatrix}
=
\boxed{
\begin{bmatrix}
2.4\\
-3.6
\end{bmatrix}}
$$

Therefore:

- $w_1$ increases: $2\rightarrow2.4$
- $w_2$ decreases: $-3\rightarrow-3.6$

---

### 30. Answer

Given:

$$
L(w_1,w_2)=w_1^2+2w_2^2
$$

Partial derivatives:

$$
\frac{\partial L}{\partial w_1}=2w_1
$$

$$
\frac{\partial L}{\partial w_2}=4w_2
$$

Therefore:

$$
\nabla L=
\begin{bmatrix}
2w_1\\
4w_2
\end{bmatrix}
$$

Start:

$$
w_0=
\begin{bmatrix}
-3\\
4
\end{bmatrix}
$$

### Update 1

Gradient:

$$
\nabla L=
\begin{bmatrix}
-6\\
16
\end{bmatrix}
$$

Update:

$$
w_1=
\begin{bmatrix}
-3\\
4
\end{bmatrix}
-
0.1
\begin{bmatrix}
-6\\
16
\end{bmatrix}
$$

$$
\boxed{
w_1=
\begin{bmatrix}
-2.4\\
2.4
\end{bmatrix}}
$$

Loss:

$$
L(-2.4,2.4)
=
(-2.4)^2+2(2.4)^2
$$

$$
\boxed{17.28}
$$

### Update 2

Gradient:

$$
\nabla L=
\begin{bmatrix}
-4.8\\
9.6
\end{bmatrix}
$$

Update:

$$
w_2=
\begin{bmatrix}
-2.4\\
2.4
\end{bmatrix}
-
0.1
\begin{bmatrix}
-4.8\\
9.6
\end{bmatrix}
$$

$$
\boxed{
w_2=
\begin{bmatrix}
-1.92\\
1.44
\end{bmatrix}}
$$

Loss:

$$
L(-1.92,1.44)=7.3728
$$

### Update 3

Gradient:

$$
\nabla L=
\begin{bmatrix}
-3.84\\
5.76
\end{bmatrix}
$$

Update:

$$
w_3=
\begin{bmatrix}
-1.92\\
1.44
\end{bmatrix}
-
0.1
\begin{bmatrix}
-3.84\\
5.76
\end{bmatrix}
$$

$$
\boxed{
w_3=
\begin{bmatrix}
-1.536\\
0.864
\end{bmatrix}}
$$

Loss:

$$
L(-1.536,0.864)=3.6864
$$

Therefore:

$$
34\rightarrow17.28\rightarrow7.3728\rightarrow3.6864
$$

The loss is decreasing.

The parameters are moving toward:

$$
\boxed{(0,0)}
$$

The negative sign makes us move opposite to the gradient, toward lower loss.

A much larger learning rate can cause the updates to become too large, potentially causing overshooting or instability.

---

# What You Should Understand Before Moving On

You should now be able to explain these in your own words:

* **Derivative:** tells how a function's output changes when its input changes.
* **Derivative sign:** positive means increasing, negative means decreasing, zero means locally flat.
* **Partial derivative:** tells how a function changes with respect to one input while keeping the others fixed.
* **Gradient:** a vector containing all the partial derivatives.
* **Gradient direction:** points toward the direction of greatest local increase.
* **Negative gradient:** points toward the direction of greatest local decrease.
* **Loss:** measures how bad the model's current parameters are.
* **Learning rate:** controls how large a parameter update is.
* **Gradient descent:** repeatedly moves parameters in the negative-gradient direction.
* **Update:**
$$
  w_{\text{new}}=w_{\text{old}}-\eta\nabla L(w)
$$  

And most importantly:

> **The gradient tells us which way to move.**

> **The learning rate tells us how far to move.**

> **Gradient descent repeats this process to reduce the loss.**
