import numpy as np

def von_mises_iteration(matrix, start_vector, num_iterations):
    """
    Führt die von Mises Iteration (Power-Methode) durch, um den größten Eigenwert
    und den zugehörigen Eigenvektor einer Matrix zu approximieren.

    Parameters:
        matrix (ndarray): Quadratische Eingabematrix.
        start_vector (ndarray): Startvektor.
        num_iterations (int): Anzahl der Iterationen.

    Returns:
        eigenvalue (float): Der dominante Eigenwert der Matrix.
        eigenvector (ndarray): Der zugehörige Eigenvektor.
    """
    # Normiere den Startvektor
    eigenvector = start_vector / np.linalg.norm(start_vector)

    for _ in range(num_iterations):
        # Multipliziere die Matrix mit dem Vektor
        next_vector = np.dot(matrix, eigenvector)

        # Berechne den neuen Eigenwert (Rayleigh-Quotient)
        eigenvalue = np.dot(next_vector, eigenvector)

        # Normiere den neuen Vektor
        eigenvector = next_vector / np.linalg.norm(next_vector)

    return eigenvalue, eigenvector

if __name__ == "__main__":
    # Beispielmatrix
    A = np.array([
        [1, 1, 0],
        [3, -1, 2],
        [2, -1, 3]
    ], dtype=float)

    # Startvektor
    x0 = np.array([1, 0, 0], dtype=float)

    # Anzahl der Iterationen
    iterations = 10

    # Führe die von Mises Iteration durch
    eigenvalue, eigenvector = von_mises_iteration(A, x0, iterations)

    # Ergebnisse ausgeben
    print("Dominanter Eigenwert:", eigenvalue)
    print("Dominanter Eigenvektor:", eigenvector)
