import sympy as sp

def vereinfachtes_newton_verfahren(f_x, start_value):
    # simplified Newton's method implementation
    if F_PRIME_X.subs(x, start_value).evalf() == 0:
        raise ValueError("Derivative is zero at x = {}".format(start_value))

    x_n = start_value

    for i in range(MAX_ITERATIONS):
        f_x_n = f_x.subs(x, x_n).evalf()
        x_n_next = x_n - f_x_n / F_PRIME_X.subs(x, start_value).evalf()
        print("Iteration {}: x_n = {}".format(i + 1, x_n_next))
        if abs(x_n_next) < EPSILON_ZERO_VALUE or abs(x_n_next - x_n) < EPSILON_TWO_VALUES:
            break
        x_n = x_n_next

    print("\nvereinfachtes Newtonverfahren - Nullstelle (geschätzt):", x_n)

    return x_n


if __name__ == "__main__":
    # replace with your values:
    x = sp.Symbol('x')
    f_x = (x ** 2) - 2
    F_PRIME_X = sp.diff(f_x, x)

    start_value = 1

    MAX_ITERATIONS = 1000
    EPSILON_ZERO_VALUE = 1e-6
    EPSILON_TWO_VALUES = 1e-6

    vereinfachtes_newton_verfahren(f_x, start_value)