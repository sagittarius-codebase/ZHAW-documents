
def number_of_positive_integers_with_digit(digit, number_of_digits):
    """
    This function returns the number of positive integers with at least a certain digit in it.

    :param int digit: number that has to be in the positive integer
    :param int number_of_digits: number of digits in the positive integer
    :return: number of positive integers with at least a certain digit in it
    :rtype: int
    """

    number_of_all_integers = 9 * 10 ** (number_of_digits - 1)
    number_of_integers_without_digit = 8 * 9 ** (number_of_digits - 1)

    return number_of_all_integers - number_of_integers_without_digit