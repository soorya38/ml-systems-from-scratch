## Normal Equation

The **normal equation** is a formula that directly calculates the best coefficients for a linear regression model — without gradient descent.

For linear regression:

$$
\hat{y} = X\theta
$$

The normal equation is:

$$
\boxed{\theta = (X^TX)^{-1}X^Ty}
$$

Where:

* \(X\) = feature matrix
* \(y\) = actual target values
* \(\theta\) = coefficients/parameters we want to find
* \(X^T\) = transpose of \(X\)
* \((X^TX)^{-1}\) = inverse of the matrix \(X^TX\)

### Why does this work?

Linear regression tries to minimize the **sum of squared errors**:

$$
J(\theta)=\|X\theta-y\|^2
$$

In other words:

> Find the line that makes the total squared distance between predictions and actual values as small as possible.

When we mathematically minimize this function, we get:

$$
X^TX\theta=X^Ty
$$

Solving for \(\theta\):

$$
\boxed{\theta=(X^TX)^{-1}X^Ty}
$$

That's the **normal equation**.

---

### Tiny example

Suppose:

| Hours studied | Score |
| ------------: | ----: |
|             1 |     2 |
|             2 |     4 |
|             3 |     6 |

We want:

$$
y=\theta_0+\theta_1x
$$

Represent \(X\) including the intercept:

$$
X=
\begin{bmatrix}
1&1\\
1&2\\
1&3
\end{bmatrix}
,\quad
y=
\begin{bmatrix}
2\\4\\6
\end{bmatrix}
$$

Then calculate:

$$
\theta=(X^TX)^{-1}X^Ty
$$

which gives:

$$
\theta=
\begin{bmatrix}
0\\2
\end{bmatrix}
$$

So the resulting model is:

$$
\boxed{\hat y=0+2x}
$$

For 4 hours:

$$
\hat y=2(4)=8
$$

**Normal equation = a mathematical shortcut that finds the optimal linear-regression coefficients directly using matrix algebra.**
