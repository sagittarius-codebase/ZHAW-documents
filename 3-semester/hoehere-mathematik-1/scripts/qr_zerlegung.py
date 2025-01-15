import numpy as np

def manual_qr_decomposition(A):
    A = A.astype(np.float64)  # Konvertiere A zu float64, um sicherzustellen, dass alle Operationen als float ausgeführt werden
    m, n = A.shape
    Q = np.zeros((m, n), dtype=np.float64)
    R = np.zeros((n, n), dtype=np.float64)
    for k in range(n):
        u = np.copy(A[:, k])
        for i in range(k):
            proj = np.dot(Q[:, i], A[:, k]) * Q[:, i]
            u -= proj
        R[k, k] = np.linalg.norm(u)
        Q[:, k] = u / R[k, k]
        for j in range(k+1, n):
            R[k, j] = np.dot(Q[:, k], A[:, j])
            A[:, j] -= R[k, j] * Q[:, k]
    return Q, R

if __name__ == "__main__":
    # Define the matrix
    A = np.array(
        [[1, 2, -1],
         [4, -2, 6],
         [3, 1, 0]],
        dtype=np.float64
    )

    matrix_q, matrix_r = manual_qr_decomposition(A)

    print("Matrix Q:\n", matrix_q)
    print("Matrix R:\n", matrix_r)

    # A = np.array(
    #     [[3, 9, 12, 12],
    #      [-2, -5, 7, 2],
    #      [6, 12, 18, 6],
    #      [3, 7, 38, 14]],
    #     dtype=float
    # )

    # Define the vector
    b = np.array([9, -4, 9], dtype=float)