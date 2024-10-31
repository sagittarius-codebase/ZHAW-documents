
def get_expected_val(x, pmf):
    """
    Calculate the expected value of a random variable.

    :param list x: list of values of the random variable
    :param list pmf: list of the probability mass function values
    :return: the expected value of the random variable
    :rtype: float
    """
    expected_val = 0
    for i in range(len(x)):
        if isinstance(pmf[i], str):
            pmf[i] = eval(pmf[i])
        expected_val += x[i] * pmf[i]
    return round(int(expected_val * 100000) / 100000, 4)