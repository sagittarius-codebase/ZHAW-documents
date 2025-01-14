import numpy as np
import math

def convergence_order(f, x0, max_iter=100, tol=1e-12):
    """
    Bestimmt die Konvergenzordnung einer Funktion.

    Parameter:
    - f: Funktion, die Nullstellen sucht (z. B. Newton-Verfahren).
    - x0: Startwert.
    - max_iter: Maximale Anzahl von Iterationen.
    - tol: Toleranzwert für Abbruchkriterium.

    Rückgabewerte:
    - Konvergenzordnung q (falls bestimmbar).
    - Liste der Fehler e_n zur Analyse.
    """
    errors = []  # Liste der Fehler |x_n - x*|
    x_n = x0     # Aktueller Wert

    for i in range(max_iter):
        x_next = f(x_n)  # Iteriere die Funktion
        error = abs(x_next - x_n)

        if error < tol:  # Abbruchkriterium
            print(f"Konvergenz nach {i+1} Iterationen erreicht.")
            break

        errors.append(error)
        x_n = x_next

    if len(errors) < 3:
        raise ValueError("Nicht genügend Daten, um die Konvergenzordnung zu bestimmen.")

    # Berechnung der Konvergenzordnung q
    q_values = []
    for i in range(1, len(errors) - 1):
        try:
            q = math.log(errors[i+1] / errors[i]) / math.log(errors[i] / errors[i-1])
            q_values.append(q)
        except ZeroDivisionError:
            continue

    # Mittelwert der q-Werte als Konvergenzordnung
    q_mean = np.mean(q_values)
    return q_mean, errors

# Beispiel: Funktion und Test
def newton_example(x):
    """Beispiel für das Newton-Verfahren bei f(x) = x^2 - 2."""
    return x - (x**2 - 2) / (2 * x)

if __name__ == "__main__":
    # Startwert für die Iteration
    x0 = 1.5

    # Konvergenzordnung bestimmen
    q, errors = convergence_order(newton_example, x0)

    print(f"Geschätzte Konvergenzordnung: {q:.4f}")
    print("Fehler in jeder Iteration:", errors)
