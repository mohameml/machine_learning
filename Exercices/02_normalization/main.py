#!/usr/bin/env python3
"""
exo : standardization  
A <- A - mean(A) / std(A)
"""
from sklearn.preprocessing import StandardScaler
import numpy as np


def standardization(matrix_a):
    """
    Standardization of a matrix.
    Each column is standardized by subtracting the mean and dividing by the std.
    """
    means_for_cols = np.mean(matrix_a, axis=0)
    std_for_cols = np.std(matrix_a, axis=0)

    # Handling cases where std is 0 to avoid division by zero
    std_for_cols[std_for_cols == 0] = 1

    # Standardize each element
    for j in range(matrix_a.shape[1]):
        for i in range(matrix_a.shape[0]):
            matrix_a[i, j] = (
                matrix_a[i, j] - means_for_cols[j]) / std_for_cols[j]

    return matrix_a


if __name__ == "__main__":

    A = np.array([
        [1.0, 2.0, 3.0],
        [3., 1., 4.],
        [5., 1., 10.]
    ])

    B = np.array([
        [1, 2, 3],
        [3, 1, 4],
        [5, 1, 10]
    ])

    A.dtype = np.float64
    scaler = StandardScaler()
    B = scaler.fit_transform(B)

    print(f"la matrice A avant la normalisation :\n {A}")
    standardization(A)
    print(f"la matrice A aprés la normalisation :\n {A}")
    print(B)
