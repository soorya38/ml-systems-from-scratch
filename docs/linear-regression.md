# Linear Regression
Linear Regression is a **supervised learning algorithm** used to predict a **continuous numerical value** (e.g., house price, salary, temperature).
It assumes there is an approximately **linear relationship** between the input(s) and the output.

**Goal:** Find the line that best fits the training data so that prediction errors are as small as possible.

---

## Mathematical Equation
$$
y = mx + c
$$

Where:
- **y** → Actual output
- **x** → Input
- **m** → Slope (how much **y** changes when **x** increases by 1 unit)
- **c** → Y-intercept (value of **y** when **x = 0**)

---

## Machine Learning Equation
$$
ŷ = wx + b
$$

Where:
- **ŷ (y-hat)** → Predicted output
- **x** → Input feature
- **w** → Weight (learned slope)
- **b** → Bias (learned intercept)

The only difference from the mathematical equation is that **w** and **b** are **learned from data** instead of being known beforehand.

---

## How Linear Regression Learns
Initially, the model starts with **random values** for **w** and **b**. <br>
For every training example:
1. Predict the output (**ŷ**)
2. Compare it with the actual output (**y**)
3. Compute the error
4. Calculate the loss (how bad the prediction is)
5. Update **w** and **b** to reduce the loss

This process is repeated until the model finds values of **w** and **b** that produce the smallest possible loss.

---

# Gradient Descent
Gradient Descent is the optimization algorithm used to learn the best values of **w** and **b**.
Its goal is to **minimize the loss function** by repeatedly updating the parameters in the direction that reduces the loss the most.<br>
The update rule is:<br>
$$
w := w - \alpha \frac{\partial L}{\partial w}
$$

$$
b := b - \alpha \frac{\partial L}{\partial b}
$$

Where:
- **α (alpha)** = Learning Rate
- **L** = Loss function

---

## Learning Rate
The **learning rate (α)** determines the **size of each update step** during gradient descent.

- **Small learning rate**
  - Smaller parameter updates
  - More stable learning
  - Usually requires more iterations
  - Can take a long time to converge

- **Large learning rate**
  - Faster updates
  - Can overshoot the minimum loss
  - May fail to converge or become unstable

The learning rate is one of the most important **hyperparameters** in machine learning.

---

# Common Terms

### Feature (X)

The input variable(s) used to make a prediction.

Example:

- House size
- Number of bedrooms
- Years of experience

---

### Label / Target (y)

The correct output that the model should learn to predict.

Example:

- House price
- Salary

---

### Prediction (ŷ)

The output produced by the model.

---

### Error (Residual)

The difference between the actual value and the predicted value.

$$
Error = y − ŷ
$$

---

### Loss Function

A function that measures **how wrong the model's predictions are** over the training data.

The optimization algorithm tries to minimize this value.

---

### Mean Squared Error (MSE)

The most common loss function for linear regression.

$$
\text{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

It is the **average of the squared prediction errors**.

Properties:

- Always non-negative
- Lower MSE means better predictions
- Squaring penalizes large errors more than small errors

---

# Overall Training Pipeline

1. Initialize **w** and **b** randomly.
2. Make predictions (**ŷ**).
3. Compute the errors (**y − ŷ**).
4. Compute the loss (typically MSE).
5. Compute the gradients.
6. Update **w** and **b** using Gradient Descent.
7. Repeat until the loss stops decreasing (or a maximum number of iterations is reached).

The final learned values of **w** and **b** define the best-fit line.