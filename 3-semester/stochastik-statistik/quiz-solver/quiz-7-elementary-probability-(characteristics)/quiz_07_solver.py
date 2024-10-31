from tabulate import tabulate
import expected_loss_win as expect_l_w
import cdf_to_characteristic as cdf_char

####################################################################################################
# Exercise: Casino with non-standard dice
####################################################################################################

# Replace the following values with the values in your quiz:
number_of_dice_rolls = 36
pay_per_roll = 4
x = [1, 2, 3, 4, 5, 6]
PMF = ["3/10", "1/6", "7/30", "2/15", "2/15", "1/30"]

# print out the table to check if the values are correct
print("Check if the values are correct:")
table = [["x"] + x, ["PMF"] + PMF]
print(tabulate(table, headers="firstrow", tablefmt="grid"))

# check the table for correctness:
assert len(x) == len(PMF), "The number of x values and PMF values must be the same."
assert sum([eval(pmf) for pmf in PMF]) == 1, "The sum of the PMF values must be 1."

# calculate the expected value:
expected_win = expect_l_w.get_expected_loss_win(x, PMF, pay_per_roll, number_of_dice_rolls)
print("When you roll the dice", number_of_dice_rolls, "times and pay", pay_per_roll, "for each roll, the expected win is:", expected_win, "\n")

