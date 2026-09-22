## Feature Scaling

**Feature scaling = transforming numerical features so they are on comparable scales.**

### 1. Why is it needed?

Suppose your data is:

| Person | Age |  Salary |
| ------ | --: | ------: |
| A      |  20 |  30,000 |
| B      |  40 |  80,000 |
| C      |  60 | 150,000 |

Salary has much larger numbers than age.

For algorithms based on **distance or magnitude** (KNN, K-Means, SVM, neural networks, etc.), salary can dominate the calculation.

---

### 2. Typical workflow

```text
Raw Dataset
     ↓
Separate features (X) and target (y)
     ↓
Split into train / validation / test
     ↓
Fit scaler ONLY on training data
     ↓
Transform training data
     ↓
Transform validation/test using the SAME scaler
     ↓
Train ML model on scaled data
     ↓
Make predictions
```

**Important:** Never fit the scaler on the entire dataset, because that causes **data leakage**.

---

### 3. Two common scaling methods

#### Standardization

Transforms values to have approximately:

* mean = 0
* standard deviation = 1

Formula:

$$
x' = \frac{x-\mu}{\sigma}
$$

Example:

```text
Age = [20, 40, 60]
mean = 40
std ≈ 16.33

20 → (20-40)/16.33 ≈ -1.22
40 → 0
60 → 1.22
```

So:

```text
[20, 40, 60]
      ↓
[-1.22, 0, 1.22]
```

---

#### Min-Max Scaling

Maps values to a fixed range, usually **0 to 1**.

$$
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
$$

Example:

```text
Age = [20, 40, 60]

20 → 0
40 → 0.5
60 → 1
```

Result:

```text
[20, 40, 60]
      ↓
[0, 0.5, 1]
```

---

### 4. What actually happens in code?

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Learn mean/std from training data
scaler.fit(X_train)

# Apply the learned transformation
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Or:

```python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Think of it as:

```text
fit()       → "Learn how to scale"
transform() → "Apply that scaling"
```

The test set **only gets `transform()`**.

---

### 5. Where does the ML model fit?

Example with KNN:

```text
Dataset
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Scaled Training Data
   ↓
KNN learns from it
   ↓
Scaled Test Data
   ↓
Prediction
```

Without scaling:

```text
Age = 25
Salary = 100,000
             ↓
Salary dominates distance
```

With scaling:

```text
Age    → 0.2
Salary → 0.4
             ↓
Both contribute comparably
```

---

# Exercises

### Exercise 1 — Min-Max

Given:

```text
X = [10, 20, 30, 40]
```

Calculate the Min-Max scaled value of:

**a)** 10
**b)** 20
**c)** 30
**d)** 40

---

### Exercise 2 — Standardization

Given:

```text
X = [10, 20, 30]
mean = 20
std = 10
```

Calculate the standardized values.

---

### Exercise 3 — Identify the mistake

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test = train_test_split(X_scaled)
```

**Question:** Why is this potentially wrong?

---

### Exercise 4 — Understand `fit` vs `transform`

Given:

```python
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Answer:

1. What does `fit()` learn?
2. Why don't we call `fit()` on `X_test`?
3. Why must the same scaler be used for both train and test?

---

### Exercise 5 — Practical

You have:

```text
Age       Salary       Experience
20        30000        1
30        60000        5
40        90000        10
```

**Question:**
Which feature is likely to dominate a distance calculation before scaling, and why?

**Core idea to remember:**

> **Feature scaling changes the numerical representation of features so that differences in units/magnitude don't unfairly influence the ML algorithm.**
