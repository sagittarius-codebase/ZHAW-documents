
####################################################################################################
# Quiz 11: Normal Distribution ZGS
####################################################################################################

# imports:
import scipy.stats as stats
import scipy.integrate as integrate

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

print(f"Either you got to your STS table and search for the value z = {abs(z):.4f}, maybe you need interpolation.")
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


####################################################################################################
# Exercise 3: binomial distribution approximation via normal distribution
print("\nExercise 3: binomial distribution approximation via normal distribution")
####################################################################################################

# Replace the following with the values of your quiz:

# in B(n, p)
number_of_repetitions = 100 # n
probability = 0.3 # p

# probability P (X ≤/< x ≤ Y)
lower_bound = 20
upper_bound = 33

# bigger than or equal-bigger than:
bigger_than = False

# Calculations:
if bigger_than:
    approx_lower_bound = lower_bound + 0.5
else:
    approx_lower_bound = lower_bound - 0.5
approx_upper_bound = upper_bound + 0.5

print("P (" + str(lower_bound) + " ≤ X ≤ " + str(upper_bound) + ") ~ P (" + str(approx_lower_bound) + " ≤ X ≤ " + str(approx_upper_bound) + ")")


####################################################################################################
# Exercise 4: number of datapoints below a function curve in a Unit square
print("\nExercise 4: number of datapoints below a function curve in a Unit square")
####################################################################################################

# Replace the following with the values of your quiz:
number_of_datapoints = 20

# for example: E(1/20 X) and V(1/20 X)
fraction_of_datapoints = 1 / 20

# function:
function = lambda x: (3 * (1 - x) * (x + 1/5)) / 2

# Calculations:
function_integral = integrate.quad(function, 0, 1)[0]
# the area can be used as the probability

expected_value = number_of_datapoints * function_integral
variance = number_of_datapoints * function_integral * (1 - function_integral)

fraction_expected_value = expected_value * fraction_of_datapoints
fraction_variance = variance * (fraction_of_datapoints ** 2)

print(f"E(1/{number_of_datapoints} X) = {fraction_expected_value:.3f}")
print(f"V(1/{number_of_datapoints} X) = {fraction_variance:.3f}")





