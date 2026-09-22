# Dummy Classifier Baseline
# Medium
# Machine Learning

# Implement a dummy (baseline) classifier that ignores feature values and produces predictions based only on the training labels and a chosen strategy. This is a useful sanity-check baseline: any real model should comfortably outperform it.

# Implement dummy_classifier(y_train, n_test, strategy, constant=None) that returns a Python list of length n_test containing predicted labels.

# Supported strategies:

# "most_frequent": every prediction equals the most frequent class in y_train. Break ties by the smallest class label.
# "constant": every prediction equals the value of constant.
# "uniform": deterministically cycle through the sorted unique classes; the prediction at position i is sorted_classes[i % k], where k is the number of unique classes.
# "stratified": produce a deterministic stratified allocation. For each class c in sorted order with empirical frequency f_c = count_c / len(y_train), assign floor(n_test * f_c) predictions to it. Distribute any remaining predictions one-by-one to the classes with the largest fractional part of n_test * f_c, breaking ties by the smallest class label. Finally, output the predictions grouped in sorted class order (all class-0 predictions first, then class-1, etc.).
# Return a plain Python list. Do not perform any rounding inside the function.

# Example:
# Input:
# y_train = [0,0,1,1,1,2], n_test = 4, strategy = "most_frequent"
# Output:
# [1, 1, 1, 1]
# Reasoning:
# Class counts are {0: 2, 1: 3, 2: 1}. The most frequent class is 1, so all 4 predictions are 1.

import numpy as np

def dummy_classifier(y_train, n_test, strategy, constant=None):

    match strategy:

        case "most_frequent":
            values, counts = np.unique(y_train, return_counts=True)

            # np.unique sorts values, so argmax naturally
            # breaks ties using the smallest label.
            label = values[np.argmax(counts)]

            return [label] * n_test

        case "constant":
            return [constant] * n_test

        case "uniform":
            classes = np.unique(y_train)

            return [
                classes[i % len(classes)]
                for i in range(n_test)
            ]

        case "stratified":
            classes, counts = np.unique(y_train, return_counts=True)

            frequencies = counts / len(y_train)
            expected = n_test * frequencies

            predictions_count = np.floor(expected).astype(int)

            remaining = n_test - predictions_count.sum()

            fractional = expected - predictions_count

            # Largest fractional part first.
            # np.unique gives sorted classes, so ties
            # automatically favor the smallest class.
            order = np.argsort(-fractional)

            for i in order[:remaining]:
                predictions_count[i] += 1

            predictions = []

            for i in range(len(classes)):
                predictions.extend(
                    [classes[i]] * predictions_count[i]
                )

            return predictions

        case _:
            raise ValueError("Unknown strategy")