
def get_expected_loss_win(x, pmf, pay_per_roll, number_of_dice_rolls):
    """
    based on the PMF and the values of x, calculate the expected loss or win,
    when rolling the dice number_of_dice_rolls times and paying pay_per_roll for each roll
    :param list x: list of values of the dice
    :param list pmf: list of the PMF values of the possible dice results
    :param int pay_per_roll: the amount of money to pay for each roll
    :param int number_of_dice_rolls: the number of dice rolls
    :return: expected loss or win
    :rtype: float
    """

    expected_win_one_roll = -pay_per_roll
    for i in range(len(x)):
        expected_win_one_roll += x[i] * eval(pmf[i])

    expected_win = expected_win_one_roll * number_of_dice_rolls
    return int(expected_win * 1000) / 1000