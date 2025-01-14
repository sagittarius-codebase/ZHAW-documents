import sympy as sp

def newton_verfahren(f_x, f_prime_x, start_value):
    # Newton's method implementation
    if f_prime_x.subs(x, start_value).evalf() == 0:
        raise ValueError("Ableitung ist Null an der Stelle x = {}".format(start_value))

    x_n = start_value
    for i in range(MAX_ITERATIONS):
        f_x_n = f_x.subs(x, x_n).evalf()
        f_prime_x_n = f_prime_x.subs(x, x_n).evalf()
        x_n_next = x_n - f_x_n / f_prime_x_n
        print("Iteration {}: x_n = {}".format(i + 1, x_n_next))
        if abs(x_n_next) < EPSILON_ZERO_VALUE or abs(x_n_next - x_n) < EPSILON_TWO_VALUES:
            break
        x_n = x_n_next

    print("\nNewtonverfahren - Nullstelle (geschätzt):", x_n)

    return x_n


if __name__ == "__main__":
    # replace with your values:
    x = sp.Symbol('x')
    f_x = (x ** 2) - 2
    f_prime_x = sp.diff(f_x, x)

    start_value = 1

    MAX_ITERATIONS = 1000
    EPSILON_ZERO_VALUE = 1e-6
    EPSILON_TWO_VALUES = 1e-6

    newton_verfahren(f_x, f_prime_x, start_value)