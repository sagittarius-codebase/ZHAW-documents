import numpy as np


def get_norms(matrix_a):
    # Calculate the 1-norm
    norm_1 = np.linalg.norm(matrix_a, ord=1)
    print(f'1-Norm: {norm_1}')

    # Calculate the 2-norm
    norm_2 = np.linalg.norm(matrix_a, ord=2)
    print(f'2-Norm: {norm_2}')

    # Calculate the infinity-norm
    norm_inf = np.linalg.norm(matrix_a, ord=np.inf)
    print(f'Infinity-Norm: {norm_inf}')


if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[-1, 1, 1],
         [1, -3, -2],
         [5, 1, 4]],
        dtype=float
    )

    # Define the vector
    b = np.array([0, 5, 3], dtype=float)

    get_norms(b)
    get_norms(A)
