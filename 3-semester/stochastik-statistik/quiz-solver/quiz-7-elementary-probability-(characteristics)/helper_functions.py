
from tabulate import tabulate
import calc_characteristics as calc_char

def print_table(x_values, pmf_values):
    """
    print out the table to check if the values are correct

    :param list x_values: list of values of the random variable
    :param list pmf_values: list of the probability mass function values
    :return: None
    """
    print("Check if the values are correct:")
    table = [["x"] + x_values, ["PMF"] + pmf_values]
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def print_expected_value(x_values, pmf):
    """
    print the expected value of a random variable

    :param list x_values: list of values of the random variable
    :param list pmf: list of the probability mass function values
    :return: None
    """
    expected_val = calc_char.get_expected_val(x_values, pmf)
    print("E(X): ", expected_val)

    expected_val_square = calc_char.get_expected_val([x**2 for x in x_values], pmf)
    print("E(X^2): ", expected_val_square)

    variance = expected_val_square - expected_val**2
    print("Var(X): ", round(int(variance * 100000) / 100000, 4), "\n")
