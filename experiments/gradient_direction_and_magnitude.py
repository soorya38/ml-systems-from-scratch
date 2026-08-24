# Gradient Direction and Magnitude

# Implement a function that calculates the magnitude and direction of a gradient vector. Given a gradient vector (which could represent the gradient of a loss function with respect to parameters), compute:

# Magnitude: The L2 norm of the gradient vector, indicating how steep the function is at that point
# Direction: The unit vector pointing in the direction of steepest ascent
# Descent Direction: The unit vector pointing in the direction of steepest descent (used in gradient descent optimization)
# The function should handle the edge case where the gradient is a zero vector (indicating a critical point). In this case, both direction vectors should be zero vectors.

# Return a dictionary containing 'magnitude' (float), 'direction' (list), and 'descent_direction' (list).

# Example:
# Input:
# gradient = [3.0, 4.0]
# Output:
# {'magnitude': 5.0, 'direction': [0.6, 0.8], 'descent_direction': [-0.6, -0.8]}

# Reasoning:
The gradient vector is [3, 4]. The magnitude is sqrt(3^2 + 4^2) = sqrt(25) = 5.0. The direction (unit vector) is [3/5, 4/5] = [0.6, 0.8], pointing in the direction of steepest ascent. The descent direction is the negation: [-0.6, -0.8], which is the direction used in gradient descent optimization.

import math

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """

    magnitude = math.sqrt(sum(x ** 2 for x in gradient))

    if magnitude == 0:
        return {
            'magnitude': 0.0,
            'direction': [0.0 for _ in gradient],
            'descent_direction': [0.0 for _ in gradient]
        }

    direction = [x / magnitude for x in gradient]
    descent_direction = [-x for x in direction]

    return {
        'magnitude': magnitude,
        'direction': direction,
        'descent_direction': descent_direction
    }
