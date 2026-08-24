# Quotient Rule for Derivatives

# Implement a function that computes the derivative of the quotient of two polynomial functions at a given point using the quotient rule.

# Given two polynomials g(x) and h(x) represented by their coefficients, compute the derivative of f(x) = g(x)/h(x) at a specific point x.

# Polynomial coefficients are given in descending order of powers. For example, [1, 2, 3] represents x^2 + 2x + 3.

# Your function should:

# Accept coefficients of the numerator polynomial g(x)
# Accept coefficients of the denominator polynomial h(x)
# Accept a point x at which to evaluate the derivative
# Return the value of f'(x) at the given point
# Assume the denominator h(x) is non-zero at the evaluation point.

# Example:
# Input:
# g_coeffs = [1, 0, 1], h_coeffs = [1, 2], x = 2.0
# Output:
# 0.6875

# Reasoning:
# g(x) = x^2 + 1, h(x) = x + 2. At x = 2: g(2) = 5, h(2) = 4, g'(2) = 4, h'(2) = 1. Using the quotient rule: f'(2) = (4 * 4 - 5 * 1) / 16 = 11/16 = 0.6875

import math

def derivative(f: list, x: float) -> float:
    """
    Calculate the derivative of a polynomial at x.

    Example:
        f = [3, 2, 1]
        represents 3x^2 + 2x + 1

        derivative = 6x + 2
    """
    ans = 0.0

    for i, coeff in enumerate(f):
        power = len(f) - 1 - i

        # Derivative of a constant is 0
        if power == 0:
            continue

        term = coeff * power

        # Avoid x ** -1
        if power - 1 == 0:
            term = term
        else:
            term *= math.pow(x, power - 1)

        ans += term

    return ans


def function(f: list, x: float) -> float:
    """
    Calculate the value of a polynomial at x.

    Example:
        f = [3, 2, 1]
        represents 3x^2 + 2x + 1
    """
    ans = 0.0

    for i, coeff in enumerate(f):
        power = len(f) - 1 - i

        term = math.pow(x, power)
        term *= coeff

        ans += term

    return ans


def quotient_rule_derivative(
    g_coeffs: list,
    h_coeffs: list,
    x: float
) -> float:
    """
    Calculate the derivative of:

        g(x) / h(x)

    using the quotient rule:

        (g'h - gh') / h^2

    Returns -1 if h(x) == 0.
    """

    g = function(g_coeffs, x)
    g_prime = derivative(g_coeffs, x)

    h = function(h_coeffs, x)
    h_prime = derivative(h_coeffs, x)

    # Division by zero
    if h == 0:
        return -1

    numerator = g_prime * h - g * h_prime
    denominator = h * h

    return numerator / denominator