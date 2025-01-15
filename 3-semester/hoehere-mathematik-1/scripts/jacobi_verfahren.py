import numpy as np


def jacobi_verfahren(matrix_a, vector_b, num_of_iterations, vector_x):
    d_matrix = np.diag(matrix_a)
    d_matrix_inv = np.diag(1 / d_matrix)
    l_matrix = np.tril(matrix_a, -1)
    r_matrix = np.triu(matrix_a, 1)

    print("D matrix:\n", d_matrix)
    print("D^-1 matrix:\n", d_matrix_inv)
    print("L matrix:\n", l_matrix)
    print("R matrix:\n", r_matrix)

    for i in range(num_of_iterations):
        vector_x = - d_matrix_inv @ ((l_matrix + r_matrix) @ vector_x - vector_b)
        print(f"x^{i + 1} = {vector_x}")


if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[4, -1, 1],
         [-2, 5, 1],
         [1, -2, 5]],
        dtype=float
    )

    # Define the vector
    b = np.array([5, 11, 12], dtype=float)

    number_of_iterations = 10
    start_vector = np.array([0, 0, 0], dtype=float)
    jacobi_verfahren(A, b, number_of_iterations, start_vector)
