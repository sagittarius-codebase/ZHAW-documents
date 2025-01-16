import numpy as np

def gauss_seidel_verfahren(matrix_a, vector_b, num_of_iterations, vector_x):
    print("Gauss-Seidel-Verfahren")
    d_matrix = np.diag(np.diag(matrix_a))  # Diagonal matrix D
    l_matrix = np.tril(matrix_a, -1)      # Lower triangular matrix L
    r_matrix = np.triu(matrix_a, 1)      # Upper triangular matrix R

    # Perform Gauss-Seidel iterations
    for iteration in range(num_of_iterations):
        for i in range(len(vector_x)):
            # Update x_i using the latest values
            sum1 = np.dot(matrix_a[i, :i], vector_x[:i])  # Contribution from L
            sum2 = np.dot(matrix_a[i, i+1:], vector_x[i+1:])  # Contribution from R
            vector_x[i] = (vector_b[i] - sum1 - sum2) / matrix_a[i, i]

        print(f"x^{iteration + 1} = {vector_x}")
    return vector_x


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
    gauss_seidel_verfahren(A, b, number_of_iterations, start_vector)
