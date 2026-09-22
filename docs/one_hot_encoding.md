### One-Hot Encoding

Converts **categorical values into 0/1 vectors**, where each category gets its own position. This prevents ML models from assuming categories have a numerical order.

**Example:**

```text
Input:
[0, 1, 2, 1, 0]

Output:
[
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 1],
 [0, 1, 0],
 [1, 0, 0]
]
```

`0 → [1,0,0]`, `1 → [0,1,0]`, `2 → [0,0,1]`.
