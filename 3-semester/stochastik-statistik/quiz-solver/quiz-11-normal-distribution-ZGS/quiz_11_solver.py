
####################################################################################################
# Quiz 11: Normal Distribution ZGS
####################################################################################################

# imports:
import scipy.stats as stats

####################################################################################################
# Exercise 1: random generator generates numbers
print("Exercise 1: random generator generates numbers")
####################################################################################################

# Replace the following with the values of your quiz:

# range:
lower_bound = 21
upper_bound = 29
# lower_bound ≤ z ≤ upper_bound

amount = 396
value = 9804
# variations of the exercise:

# at maximum or at minimum:
at_maximum = True

# sum or arithmetic mean:
is_sum = True

# Calculations:
expected_val = (lower_bound + upper_bound) / 2

variation = ((upper_bound - lower_bound) * (upper_bound - lower_bound + 2)) / 12

summed_expected_val = amount * expected_val
summed_variation = amount * variation
summed_standard_deviation = summed_variation ** 0.5

mean_expected_val = expected_val
mean_variation = variation
mean_standard_deviation = mean_variation ** 0.5


if is_sum:
    z = (value - summed_expected_val) / summed_standard_deviation
else:
    z = (value - mean_expected_val) / mean_standard_deviation

p = stats.norm.cdf(z) if at_maximum else 1 - stats.norm.cdf(z)

comparison = "≤" if at_maximum else ">"
output_type = "X" if is_sum else "X̄"

print(f"Either you got to your STS table and search for the value z = {abs(z):.2f}, maybe you need interpolation.")
print(f"Or you just use this result: P({output_type} {comparison} {value:.2f}) = {p:.3f}")


####################################################################################################
# Exercise 2: expected value and variance based on the given values
print("\nExercise 2: expected value and variance based on the given values")
################################################################################################

# Replace the following with the values of your quiz:
number_of_variables = 40
expected_value = 8
variance = 6

# differentiate between sum and mean:
is_sum = True

# Calculations:
summed_expected_val = number_of_variables * expected_value
summed_variance = number_of_variables * variance

mean_expected_val = expected_value
mean_variance = variance / number_of_variables

if is_sum:
    print(f"Expected value of the sum: {summed_expected_val}")
    print(f"Variance of the sum: {summed_variance}")
else:
    print(f"Expected value of the mean: {mean_expected_val}")
    print(f"Variance of the mean: {mean_variance}")

