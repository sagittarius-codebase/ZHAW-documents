import numpy as np


def calc_abs_and_rel_error(matrix_a, vector_b, a_max_dev, b_max_dev):

    # Calculate Conditions number of A
    matrix_a_norm_inf = np.linalg.norm(matrix_a, ord=np.inf)
    matrix_a_inv = np.linalg.inv(matrix_a)
    matrix_a_inv_norm_inf = np.linalg.norm(matrix_a_inv, ord=np.inf)
    condition_number_a = matrix_a_norm_inf * matrix_a_inv_norm_inf
    print(f'Condition number of A: {condition_number_a:.2f}\n')

    # absolute error
    b_abs_error = b_max_dev
    x_abs_error = matrix_a_inv_norm_inf * b_abs_error
    abs_error_factor = x_abs_error / b_abs_error
    print(f"Absolute error of x is: {x_abs_error:.2f} so the factor is: {abs_error_factor:.2f}")

    # relative error
    b_rel_error = b_max_dev / np.linalg.norm(vector_b, ord=np.inf)

    if a_max_dev == 0:
        x_rel_error = condition_number_a * b_rel_error
        rel_error_factor = x_rel_error / b_rel_error
    else:
        a_max_dev_summed = a_max_dev * len(matrix_a)
        a_rel_error = a_max_dev_summed / matrix_a_norm_inf
        if condition_number_a * a_rel_error > 1:
            print("The relative error of x can't be calculated because the condition number is greater than 1")
            exit()
        x_rel_error = (condition_number_a / (1 - condition_number_a * a_rel_error)) * (b_rel_error + a_rel_error)
        rel_error_factor = x_rel_error / b_rel_error

    print(f"Relative error of x is: {x_rel_error:.2f} so the factor is: {rel_error_factor:.2f}")




if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[2, 4],
         [4, 8.1]],
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
    b = np.array([1, 1.5], dtype=float)

    b_max_deviation = 0.1
    A_max_deviation = 0.003

    calc_abs_and_rel_error(A, b, A_max_deviation, b_max_deviation)