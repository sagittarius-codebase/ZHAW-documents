import numpy as np


def gauss_jordan(matrix_a, vector_b):

    for i in range(len(matrix_a)):

        # Check if pivot element is zero, if so try to swap rows
        if matrix_a[i, i] == 0:
            for j in range(i + 1, len(matrix_a)):
                if matrix_a[j, i] != 0:
                    matrix_a[[i, j]] = matrix_a[[j, i]]
                    vector_b[[i, j]] = vector_b[[j, i]]
                    break
                raise ValueError("Matrix is not regular and cannot be solved.")

        # get leading ones
        factor = matrix_a[i, i]
        matrix_a[i] = matrix_a[i] / factor
        vector_b[i] = vector_b[i] / factor

        # Elimination step
        for j in range(i + 1, len(matrix_a)):
            factor = matrix_a[j, i] / matrix_a[i, i]
            matrix_a[j] = matrix_a[j] - factor * matrix_a[i]
            vector_b[j] = vector_b[j] - factor * vector_b[i]

    r_matrix = matrix_a.copy()
    print("Matrix A after forward elimination:\n", matrix_a)
    print("Vector b after forward elimination:\n", vector_b)

    # Backward substitution
    solutions = []

    for i in range(len(matrix_a) - 1, -1, -1):
        vector_element = vector_b[i]
        matrix_elements = []
        for sol_index, j in enumerate(range(i + 1, len(matrix_a))):
            matrix_elements.append(matrix_a[i, j] * solutions[sol_index])

        solutions.insert(0, vector_element - sum(matrix_elements))

    for i, sol in enumerate(solutions):
        print(f"x{i+1} = {sol:.3f}")

    return solutions, r_matrix, vector_b


if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[1, 5, 6],
         [7, 9, 6],
         [2, 3, 4]],
        dtype=float
    )

    # Define the vector
    b = np.array([29, 43, 20], dtype=float)

    # Solve the system of linear equations with numpy
    x = np.linalg.solve(A, b)
    print(f"Numpy solution: {x}")

    # custom implementation of Gauss-Jordan elimination:
    x_custom, _, _ = gauss_jordan(A, b)