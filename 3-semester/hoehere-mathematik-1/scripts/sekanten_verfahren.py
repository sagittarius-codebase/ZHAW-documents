import sympy as sp


def sekanten_verfahren(f_x, start_value_1, start_value_2):
    # Sekanten-Verfahren implementation
    x_n_minus_1 = start_value_1
    x_n = start_value_2

    for i in range(MAX_ITERATIONS):
        f_x_n_minus_1 = f_x.subs(x, x_n_minus_1).evalf()
        f_x_n = f_x.subs(x, x_n).evalf()

        x_n_plus_1 = x_n - f_x_n * ((x_n - x_n_minus_1) / (f_x_n - f_x_n_minus_1))
        print("Iteration {}: x_n = {}".format(i + 1, x_n_plus_1))
        if abs(x_n_plus_1 - x_n) < EPSILON_ZERO_VALUE or abs(x_n_plus_1 - x_n) < EPSILON_TWO_VALUES:
            break
        x_n_minus_1 = x_n
        x_n = x_n_plus_1

    print("\nSekantenverfahren - Nullstelle (geschätzt):", x_n)

    return x_n


if __name__ == "__main__":
    # replace with your values:
    x = sp.Symbol('x')
    f_x = (x ** 2) - 2

    # two starting values
    start_value_1 = 1
    start_value_2 = 2

    MAX_ITERATIONS = 1000
    EPSILON_ZERO_VALUE = 1e-6
    EPSILON_TWO_VALUES = 1e-6

    sekanten_verfahren(f_x, start_value_1, start_value_2)
