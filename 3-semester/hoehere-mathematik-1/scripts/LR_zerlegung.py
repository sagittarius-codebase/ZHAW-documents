import numpy as np


def lr_zerlegung(matrix_a, vector_b):
    n = len(matrix_a)
    matrix_l = np.eye(n)
    matrix_p = np.eye(n)

    # Forward elimination
    for i in range(len(matrix_a)):

        # pivotisation to get the biggest element in column:
        max_row = np.argmax(np.abs(matrix_a[i:, i])) + i
        # Swap rows
        matrix_a[[i, max_row]] = matrix_a[[max_row, i]]
        matrix_p[[i, max_row]] = matrix_p[[max_row, i]]
        # in L matrix we only swap the row elements in the current column
        matrix_l[[i, max_row], :i] = matrix_l[[max_row, i], :i]

        if matrix_a[i, i] == 0:
            raise ValueError("Matrix is singular and cannot be solved.")

        # Elimination step
        for j in range(i + 1, len(matrix_a)):
            factor = matrix_a[j, i] / matrix_a[i, i]
            matrix_l[j, i] = factor
            matrix_a[j] = matrix_a[j] - factor * matrix_a[i]

    matrix_r = matrix_a.copy()
    print("R matrix after forward elimination:\n", matrix_r)
    print("L matrix after forward elimination:\n", matrix_l)
    print("P matrix after forward elimination:\n", matrix_p)

    # Solving the system of equations
    # 1. Solve Pb
    vector_b = np.dot(matrix_p, vector_b)
    print("Vector b after solving Pb:\n", vector_b)

    # 2. Solve Ly = Pb through forward substitution
    vector_y = np.zeros(n)
    for i in range(n):
        subtract = 0
        for j in range(i):
            subtract += matrix_l[i, j] * vector_y[j]
        vector_y[i] = vector_b[i] - subtract

    print("Vector y after solving Ly = Pb:\n", vector_y)

    # 3. Solve Rx = y through backward substitution
    vector_x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        subtract = 0
        for j in range(i + 1, n):
            subtract += matrix_r[i, j] * vector_x[j]
        vector_x[i] = (vector_y[i] - subtract) / matrix_r[i, i]

    print("Vector x after solving Rx = y:\n", vector_x)


    return matrix_r, matrix_l, matrix_p, vector_x

if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[-1, 1, 1],
         [1, -3, -2],
         [5, 1, 4]],
        dtype=float
    )

    # A = np.array(
    #     [[3, 9, 12, 12],
    #      [-2, -5, 7, 2],
    #      [6, 12, 18, 6],
    #      [3, 7, 38, 14]],
    #     dtype=float
    # )

    # Define the vector
    b = np.array([0, 5, 3], dtype=float)

    r_matrix, l_matrix, p_matrix, x_vector = lr_zerlegung(A, b)