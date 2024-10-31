import expected_loss_win as expect_l_w
import plot_cdf_to_characteristic as cdf_char
import calc_characteristics as calc_char
import helper_functions as helper

SUM_MUSST_BE_1 = "The sum of the PMF values must be 1."

MUST_BE_THE_SAME = "The number of x values and PMF values must be the same."

####################################################################################################
# Exercise: Casino with non-standard dice
####################################################################################################

print("Exercise: Casino with non-standard dice\n")

# Replace the following values with the values in your quiz:
number_of_dice_rolls = 36
pay_per_roll = 4
x = [1, 2, 3, 4, 5, 6]
PMF = ["3/10", "1/6", "7/30", "2/15", "2/15", "1/30"]

# print out the table to check if the values are correct
helper.print_table(x, PMF)

# check the table for correctness:
assert len(x) == len(PMF), MUST_BE_THE_SAME
assert sum([eval(pmf) for pmf in PMF]) == 1, SUM_MUSST_BE_1

# calculate the expected value:
expected_win = expect_l_w.get_expected_loss_win(x, PMF, pay_per_roll, number_of_dice_rolls)
print("When you roll the dice", number_of_dice_rolls, "times and pay", pay_per_roll, "for each roll, the expected win is:", expected_win, "\n")

####################################################################################################
# Exercise: Graphic with CDF
####################################################################################################
print("#" * 100 + "\n")

print("Exercise: Graphic with CDF\n")

# Replace the following values with the values in your quiz:
# Read out the PMF values from the graphic you see in your quiz,
# by taking the jump-amounts of the CDF values.
# The x-values are the values where the CDF jumps.
# the PMF values are the jump-amounts of the CDF values.

x_values = [2, 4, 5, 6, 8]
PMF_values = [0.2, 0.1, 0.2, 0.1, 0.4]

assert len(x_values) == len(PMF_values), MUST_BE_THE_SAME
assert sum(PMF_values) == 1, SUM_MUSST_BE_1

cdf_char.plot_cdf(PMF_values, x_values)
print("The CDF graphic is shown. Compare it with the graphic in your quiz.\n")

helper.print_expected_value(x_values, PMF_values)

####################################################################################################
# Exercise: expected value, expected value of the square, and variance of a random variable
####################################################################################################
print("#" * 100 + "\n")

print("Exercise: expected value, expected value of the square, and variance of a random variable\n")

# Replace the following values with the values in your quiz:
x_values = [1, 2, 3, 7]
PMF_values = ["0.1", "0.2", "0.6", "0.1"]

# print out the table to check if the values are correct
helper.print_table(x_values, PMF_values)


# check the table for correctness:
assert len(x_values) == len(PMF_values), MUST_BE_THE_SAME
assert sum([eval(pmf) for pmf in PMF_values]) == 1, SUM_MUSST_BE_1

# print the expected value of the random variable
helper.print_expected_value(x_values, PMF_values)

####################################################################################################
# Exercise: expected value of a random variable
####################################################################################################
print("#" * 100 + "\n")

print("Exercise: ONLY expected value of a random variable\n")

# Replace the following values with the values in your quiz:
x_values = [3, 4, 5, 6, 7]
PMF_values = ["0.1", "0.1", "0.1", "0.5", "0.2"]

# print out the table to check if the values are correct
helper.print_table(x_values, PMF_values)

# check the table for correctness:
assert len(x_values) == len(PMF_values), MUST_BE_THE_SAME
assert sum([eval(pmf) for pmf in PMF_values]) == 1, SUM_MUSST_BE_1

# print the expected value of the random variable
expected_val = calc_char.get_expected_val(x_values, PMF_values)
print("E(X): ", expected_val)

