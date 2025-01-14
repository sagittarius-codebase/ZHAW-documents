import numpy as np
import sympy as sp


def fixpunkt_iteration(f_x, f_prime_x, a, b):

    # 1. Check Banach's Fixed Point Theorem -> Check if f(I) ⊆ I
    f_i = [f_x.subs(x, a).evalf(), f_x.subs(x, b).evalf()]
    print(f"f(a) = {f_i[0]:.10f}, f(b) = {f_i[1]:.10f}")
    if all(a <= val <= b for val in f_i):
        print("f bildet sich in I selber ab!\n")
    else:
        print("f bildet sich nicht in I selber ab! STOP!")
        exit()

    # Calculate Lipschitz constant λ
    # Lipschitz constant is the maximum of |f'(x)| in the interval [1, 2]
    f_prime_vals = [f_prime_x.subs(x, a).evalf(), f_prime_x.subs(x, b).evalf()]
    lambda_ = max(abs(val) for val in f_prime_vals)
    if lambda_ >= 1:
        print("Lipschitz-Konstante λ >= 1! STOP!")
        exit()
    print(f"Lipschitz-Konstante λ = {lambda_:.10f}\n")


    # 2. A-priori error and maximum number of iterations
    epsilon = 1e-6  # gewünschte Genauigkeit
    x0 = (a + b) / 2  # Startwert

    # erster Schritt x1
    x1 = f_x.subs(x, x0).evalf()

    # Maximum number of iterations
    n_max = np.ceil(sp.log((epsilon * (1 - lambda_)) / abs(x1 - x0)) / sp.log(lambda_))
    print(f"Maximale Iterationsanzahl für gewünschte Genauigkeit: {n_max}")

    # A-priori error
    epsilon_apriori = (lambda_ ** n_max) / (1 - lambda_) * abs(x1 - x0)
    print(f"A-priori Fehler: {epsilon_apriori:.10f}\n")

    # Iterative calculation of the fixed point
    x_n = x0
    all_iterations = []
    for i in range(int(n_max)):
        x_n = f_x.subs(x, x_n).evalf()
        all_iterations.append(x_n)
        print(f"Iteration {i+1}: x_n = {x_n}")

    print(f"\nFixpunkt (geschätzt): {x_n}\n")


    # 3. A-posteriori error
    # Calculate the a-posteriori error
    epsilon_apost = lambda_ / (1 - lambda_) * abs(all_iterations[-1] - all_iterations[-2])
    print(f"A-posteriori Fehler: {epsilon_apost:.10f}")

    return x_n, epsilon_apriori, epsilon_apost


if __name__ == "__main__":
    # replace with your values:
    x = sp.Symbol('x')

    # make sure that function is in fixed point form -> x = f(x)
    f_x = sp.log(x + 2)
    f_prime_x = sp.diff(f_x, x)

    # Interval I = [1, 2]
    a, b = 1, 2

    fixpunkt_iteration(f_x, f_prime_x, a, b)